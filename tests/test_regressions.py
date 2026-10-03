import ast
import json
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import MagicMock
ROOT = Path(__file__).resolve().parents[1]

def definitions(filename, names, namespace):
    path = ROOT / filename
    if path.suffix == '.ipynb':
        nb = json.loads(path.read_text())
        text = '\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type'] == 'code')
        text = '\n'.join(line if not line.startswith(('!', '%', 'pip install')) else '# '+line for line in text.splitlines())
    else:
        text = path.read_text()
    tree = ast.parse(text)
    body = [ast.ImportFrom(module='__future__', names=[ast.alias(name='annotations')], level=0)]
    body += [node for node in tree.body if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in names]
    module = ast.fix_missing_locations(ast.Module(body=body, type_ignores=[]))
    exec(compile(module, str(path), 'exec'), namespace)
    return namespace
class CausalRegressionTests(unittest.TestCase):
    def test_notebook_uses_fitted_outcome_models(self):
        n=json.loads((ROOT/'Individual_Assignment_2_Causal_Inference.ipynb').read_text())
        text=''.join(n['cells'][3]['source'])
        self.assertNotIn('temp_learner.fit(X, treatment, y)',text)
        self.assertIn('xgb_model.models_c[1]',text)
        self.assertIn('xgb_model.models_t[1]',text)
        # Exercise the actual plotting block with fitted-estimator stand-ins.
        a=text.index('# Inspect fitted outcome');b=text.index('"""\n## 4.',a)
        import matplotlib;matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        estimator=SimpleNamespace(feature_importances_=[.1,.2,.3,.2,.2])
        exec(text[a:b],dict(plt=plt,common_features=['a','b','c','d','e'],
            xgb_model=SimpleNamespace(models_c={1:estimator},models_t={1:estimator})))
