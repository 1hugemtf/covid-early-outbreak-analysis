"""Execute the notebook from scratch and verify the COVID snapshot analysis and charts."""
from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager

root = Path(__file__).resolve().parent
nb = nbformat.read(root / "notebook.ipynb", as_version=4)
nbformat.validate(nb)
for cell in nb.cells:
    if cell.cell_type == "code":
        cell.outputs = []
        cell.execution_count = None
nb.cells.append(nbformat.v4.new_code_cell("\nassert len(world) == 56 and world.date.is_unique\nassert world.date.equals(pd.Series(pd.date_range('2020-01-22','2020-03-17'),name='date'))\nassert not country_rows.duplicated(['country','province','date']).any()\nassert not countries.duplicated(['country','date']).any()\nassert countries.groupby('country').size().eq(56).all()\nassert reconciliation[['World difference','Outside difference']].eq(0).all().all()\nassert world_series.iloc[-1] == 197146\nassert regional.iloc[-1].to_dict() == {'China': 81058, 'Outside China': 116088}\nassert crossover == pd.Timestamp('2020-03-15')\nassert top7.country.tolist() == ['Italy','Iran','Spain','Germany','Korea, South','France','US']\nassert top7.cum_cases.tolist() == [31506,16169,11748,9257,8320,7699,6421]\nassert len(countries)==8456 and countries.cum_cases.ge(0).all()\nassert len(daily_changes)==55 and daily_changes.index.min()==pd.Timestamp('2020-01-23')\nassert rolling.iloc[:6].isna().all().all()\nnp.testing.assert_allclose(rolling.iloc[6], daily_changes.iloc[:7].mean())\nassert regional['Outside China'].gt(0).all()\nassert raw_confirmed.date.max()==pd.Timestamp('2020-03-16')\nassert audit.loc['2020-03-16','Difference: raw minus analysis']==15\nfixture=pd.DataFrame({'country':['X','X','X','X'],'date':pd.to_datetime(['2020-01-01','2020-01-01','2020-01-02','2020-01-02']),'cases':[5,3,-2,1],'cum_cases':[999]*4})\nassert aggregate_country_rows(fixture).cum_cases.tolist()==[8,7]\nassert aggregate_country_rows(fixture.sample(frac=1,random_state=7)).cum_cases.tolist()==[8,7]\nfor name in ['outbreak_overview.png','daily_reported_changes.png','country_comparison.png','linear_and_log_scales.png']:\n assert Path(name).is_file() and Path(name).stat().st_size>10000\nprint('PASS: reconciliation, province aggregation, negative corrections, rankings, dates, rolling means and charts')\n"))
km = KernelManager(kernel_name="python3")
km.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
client = NotebookClient(nb, km=km, timeout=180,
    resources={"metadata": {"path": str(root)}})
try:
    client.execute()
finally:
    if km.has_kernel:
        km.shutdown_kernel(now=True)
nb.cells.pop()
nbformat.write(nb, root / "notebook.ipynb")
print("PASS: notebook executed from cleared outputs; COVID snapshot and chart checks passed.")
