from html_maker import html_string
from contextlib import suppress
from flask import Flask #pip install flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import session
from flask_wtf import FlaskForm #pip install -U Flask-WTF
# from flask_wtf import Form  ----- se não funcionar o acima, lembrar de mudar na Class abaixo
from wtforms import StringField, IntegerField, RadioField, SelectField, TextAreaField #pip install WTForms
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'seu_codigo_magnifico_aqui'


class Authorize_cx_form(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    idade = StringField()
    # justificativa = StringField(u'justificativa', widget=TextArea())
    justificativa = TextAreaField('justificativa', validators=[DataRequired()])  # , render_kw={"rows": 70, "cols": 11})
    num_tempo = StringField()
    tempo_fields = [("anos", "Anos"), ("meses", "Meses"), ("dias", "Dias")]
    unity_tempo = SelectField('unity_tempo', choices=tempo_fields)
    exames = StringField("exames")
    hipotese = StringField("hipotese")
    cid = StringField("cid")
    carater_fields = [("internacao", "Internação"), ("ambulatorio", "Ambulatório")]
    carater = RadioField('carater', choices=carater_fields)
    duracao = StringField()
    anestesia_fields = [('local', 'Local'), ('geral', 'Geral')]
    anestesia = RadioField('anestesia', choices=anestesia_fields)
    gravidade_fields = [('urgencia', 'Urgência'), ('eletiva', 'Eletiva')]
    gravidade = RadioField('gravidade', choices=gravidade_fields)
    code1 = StringField()
    code2 = StringField()
    code3 = StringField()
    code4 = StringField()
    code5 = StringField()
    code6 = StringField()
    code7 = StringField()
    code8 = StringField()
    cx1 = StringField()
    cx2 = StringField()
    cx3 = StringField()
    cx4 = StringField()
    cx5 = StringField()
    cx6 = StringField()
    cx7 = StringField()
    cx8 = StringField()
    qx1 = StringField()
    qx2 = StringField()
    qx3 = StringField()
    qx4 = StringField()
    qx5 = StringField()
    qx6 = StringField()
    qx7 = StringField()
    qx8 = StringField()
    opme1 = StringField()
    opme2 = StringField()
    opme3 = StringField()
    opme4 = StringField()
    opme5 = StringField()
    opme6 = StringField()
    forn1 = StringField()
    forn2 = StringField()
    forn3 = StringField()
    forn4 = StringField()
    forn5 = StringField()
    forn6 = StringField()
    qo1 = StringField()
    qo2 = StringField()
    qo3 = StringField()
    qo4 = StringField()
    qo5 = StringField()
    qo6 = StringField()


def kill_session():
    session_keys = [
        'nome', 'idade', 'justificativa', 'anos', 'meses', 'dias', 'exames', 'hipotese', 'cid', 'carater', 'duracao',
        'anestesia', 'gravidade',
        'cx1', 'cx2', 'cx3', 'cx4', 'cx5', 'cx6', 'cx7', 'cx8',
        'code1', 'code2', 'code3', 'code4', 'code5', 'code6', 'code7', 'code8',
        'qx1', 'qx2', 'qx3', 'qx4', 'qx5', 'qx6', 'qx7', 'qx8',
        'opme1', 'opme2', 'opme3', 'opme4', 'opme5', 'opme6',
        'forn1', 'forn2', 'forn3', 'forn4', 'forn5', 'forn6',
        'qo1', 'qo2', 'qo3', 'qo4', 'qo5', 'qo6'
    ]
    with suppress(Exception):
        for key in session_keys:
            session.pop(key)
        #session.clear()


@app.route("/cx_form", methods=["GET", "POST"])
def cx_form():
    from html_maker import html_string
    kill_session()
    form = Authorize_cx_form()
    if form.validate_on_submit():
        print(form)
        session['user'] = 'user in'
        session['nome'] = form.nome.data
        session['idade'] = form.idade.data
        session['justificativa'] = form.justificativa.data
        session['num_tempo'] = form.num_tempo.data
        session['unity_tempo'] = form.unity_tempo.data
        session['exames'] = form.exames.data
        session['hipotese'] = form.hipotese.data
        session['cid'] = form.cid.data
        session['carater'] = form.carater.data
        session['duracao'] = form.duracao.data
        session['anestesia'] = form.anestesia.data
        session['gravidade'] = form.anestesia.data
        # se der erro daqui em diante, fazer Try / Except statements
        try:
            session['code1'] = form.code1.data
        except:
            session['code1'] = ""
        try:
            session['code2'] = form.code2.data
        except:
            session['code2'] = ""
        try:
            session['code3'] = form.code3.data
        except:
            session['code3'] = ""
        try:
            session['code4'] = form.code4.data
        except:
            session['code4'] = ""
        try:
            session['code5'] = form.code5.data
        except:
            session['code5'] = ""
        try:
            session['code6'] = form.code6.data
        except:
            session['code6'] = ""
        try:
            session['code7'] = form.code7.data
        except:
            session['code7'] = ""
        try:
            session['code8'] = form.code8.data
        except:
            session['code8'] = ""
        try:
            session['cx1'] = form.cx1.data
        except:
            session['cx1'] = "Sem códigos solicitados no verso."
        if form.cx1.data == "":
            session['cx1'] = "Sem códigos solicitados no verso."
        try:
            session['cx2'] = form.cx2.data
        except:
            session['cx2'] = ""
        try:
            session['cx3'] = form.cx3.data
        except:
            session['cx3'] = ""
        try:
            session['cx4'] = form.cx4.data
        except:
            session['cx4'] = ""
        try:
            session['cx5'] = form.cx5.data
        except:
            session['cx5'] = ""
        try:
            session['cx6'] = form.cx6.data
        except:
            session['cx6'] = ""
        try:
            session['cx7'] = form.cx7.data
        except:
            session['cx7'] = ""
        try:
            session['cx8'] = form.cx8.data
        except:
            session['cx8'] = ""
        try:
            session['qx1'] = form.qx1.data
        except:
            session['qx1'] = ""
        try:
            session['qx2'] = form.qx2.data
        except:
            session['qx2'] = ""
        try:
            session['qx3'] = form.qx3.data
        except:
            session['qx3'] = ""
        try:
            session['qx4'] = form.qx4.data
        except:
            session['qx4'] = ""
        try:
            session['qx5'] = form.qx5.data
        except:
            session['qx5'] = ""
        try:
            session['qx6'] = form.qx6.data
        except:
            session['qx6'] = ""
        try:
            session['qx7'] = form.qx7.data
        except:
            session['qx7'] = ""
        try:
            session['qx8'] = form.qx8.data
        except:
            session['qx8'] = ""
        try:
            session['opme1'] = form.opme1.data
        except:
            session['opme1'] = "Sem OPME para o presente exame."
        if form.opme1.data == "":
            session['opme1'] = "Sem OPME para o presente exame."
        try:
            session['opme2'] = form.opme2.data
        except:
            session['opme2'] = ""
        try:
            session['opme3'] = form.opme3.data
        except:
            session['opme3'] = ""
        try:
            session['opme4'] = form.opme4.data
        except:
            session['opme4'] = ""
        try:
            session['opme5'] = form.opme5.data
        except:
            session['opme5'] = ""
        try:
            session['opme6'] = form.opme6.data
        except:
            session['opme6'] = ""
        try:
            session['forn1'] = form.forn1.data
        except:
            session['forn1'] = ""
        try:
            session['forn2'] = form.forn2.data
        except:
            session['forn2'] = ""
        try:
            session['forn3'] = form.forn3.data
        except:
            session['forn3'] = ""
        try:
            session['forn4'] = form.forn4.data
        except:
            session['forn4'] = ""
        try:
            session['forn5'] = form.forn5.data
        except:
            session['forn5'] = ""
        try:
            session['forn6'] = form.forn6.data
        except:
            session['forn6'] = ""
        try:
            session['qo1'] = form.qo1.data
        except:
            session['qo1'] = ""
        try:
            session['qo2'] = form.qo2.data
        except:
            session['qo2'] = ""
        try:
            session['qo3'] = form.qo3.data
        except:
            session['qo3'] = ""
        try:
            session['qo4'] = form.qo4.data
        except:
            session['qo4'] = ""
        try:
            session['qo5'] = form.qo5.data
        except:
            session['qo5'] = ""
        try:
            session['qo6'] = form.qo6.data
        except:
            session['qo6'] = ""
        return redirect(url_for('print_form'))
    else:
        print('erro', form.errors)
        return render_template('cx_form_maker.html', form=form)


@app.route("/print_form", methods=["GET", "POST"])
def print_form():
    if "user" not in session:
        return redirect(url_for("cx_form"))
    nome = session['nome']
    idade = session['idade']
    justificativa = session['justificativa']
    num_tempo = session['num_tempo']
    unity_tempo = session['unity_tempo']

    if unity_tempo == "dias":
        anos = ""
        meses= ""
        dias = num_tempo
    elif unity_tempo == "meses":
        anos = ""
        meses = num_tempo
        dias = ""
    else:
        anos = num_tempo
        meses = ""
        dias = ""

    exames = session['exames']
    hipotese = session['hipotese']
    cid = session['cid']
    carater = session['carater']
    duracao = session['duracao']
    anestesia = session['anestesia']
    gravidade = session['gravidade']
    with suppress(Exception):
        code1, code2, code3, code4, code5, code6, code7, code8 = session['code1'], session['code2'], session['code3'], session['code4'], session['code5'], session['code6'], session['code7'], session['code8']
        cx1, cx2, cx3, cx4, cx5, cx6, cx7, cx8 = session['cx1'], session['cx2'], session['cx3'], session['cx4'], session['cx5'], session['cx6'], session['cx7'], session['cx8']
        qx1, qx2, qx3, qx4, qx5, qx6, qx7, qx8 = session['qx1'], session['qx2'], session['qx3'], session['qx4'], session['qx5'], session['qx6'], session['qx7'], session['qx8']
        opme1, opme2, opme3, opme4, opme5, opme6 = session['opme1'], session['opme2'], session['opme3'], session['opme4'], session['opme5'], session['opme6']
        forn1, forn2, forn3, forn4, forn5, forn6 = session['forn1'], session['forn2'], session['forn3'], session['forn4'], session['forn5'], session['forn6']
        qo1, qo2,qo3,qo4,qo5,qo6 = session['qo1'], session['qo2'], session['qo3'], session['qo4'], session['qo5'], session['qo6']

    form_string = html_string(nome, idade, justificativa, anos, meses, dias, exames, hipotese, cid, carater, duracao,
                              anestesia, gravidade,
                              cx1, cx2, cx3, cx4, cx5, cx6, cx7, cx8,
                              code1, code2, code3, code4, code5, code6, code7, code8,
                              qx1, qx2, qx3, qx4, qx5, qx6, qx7, qx8,
                              opme1, opme2, opme3, opme4, opme5, opme6,
                              forn1, forn2, forn3, forn4, forn5, forn6,
                              qo1, qo2, qo3, qo4, qo5, qo6)
    return form_string


if __name__ == "__main__":
    app.run()
