import csv
import plotly.graph_objs as go
from plotly.subplots import make_subplots


def csv_dict_reader(file_obj):
    vacancies = []
    reader = csv.DictReader(file_obj, delimiter=',')
    for line in reader:
        try:
            vacancies.append(int(line["Salary"]))
        except Exception as e:
            print(e)
            continue
    return vacancies


if __name__ == "__main__":
    with open("../lab1314/export.csv", encoding="utf-8") as f_obj:
        shoto = csv_dict_reader(f_obj)
    with open("../lab1314/export2.csv", encoding="utf-8") as f_obj:
        shoto2 = csv_dict_reader(f_obj)
    fig = make_subplots(
        rows=2, cols=1,
        subplot_titles=("Первая зависимость", "Вторая зависимость"))
    fig.add_trace(go.Scatter(x=[i for i in range(len(shoto))], y=shoto, name="Зависимость зарплат по Java"), row=1,
                  col=1)
    fig.add_trace(go.Scatter(x=[i for i in range(len(shoto))], y=shoto2, name="Зависимость зарплат по Java"), row=2,
                  col=1)
    fig.update_xaxes(title_text="Номер", row=1, col=1)
    fig.update_xaxes(title_text="Номер", row=2, col=1)
    fig.update_yaxes(title_text="Зарплата", row=1, col=1)
    fig.update_yaxes(title_text="Зарплата", row=2, col=1)
    fig.update_traces(hoverinfo="all", hovertemplate="Номер: %{x}<br>Зарплата: %{y}")
    fig.write_html("second_first.html")
