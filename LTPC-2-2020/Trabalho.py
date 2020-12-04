from flask import Flask, render_template

app = Flask(_name_)

@app.route('/')
def primeira_pagina():
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Opções de Filmes</title>
        </head>
        <body leftmargin="60">
            <h1>DECIDA QUAL FILME ASSISTIR</h1>
            <a href="http://lucasladislaualmeida.pythonanywhere.com/"><h3>Home</h3></a>
            <h2>Gêneros de Filmes por Classificação Indicativa</h2>
            <p>Neste site será mostrado uma lista de filmes indicados para você assistir com base no gênero e a classificação indicativa escolhida .</p>
            <ul>
                 <a href="http://lucasladislaualmeida.pythonanywhere.com/idadeacao"><li>Ação</li></a>
                 <a href="http://lucasladislaualmeida.pythonanywhere.com/idadeanimacao"><li>Animação</li></a>
                 <a href="http://lucasladislaualmeida.pythonanywhere.com/idadecomedia"><li>Comédia</li></a>
                 <a href="http://lucasladislaualmeida.pythonanywhere.com/idadedrama"><li>Drama</li></a>
                 <a href="http://lucasladislaualmeida.pythonanywhere.com/idadesuspense"><li>Suspense</li></a>
                 <a href="http://lucasladislaualmeida.pythonanywhere.com/idadeterror"><li>Terror</li></a>
            </ul>
        </body>
    </html>
    """

@app.route('/idadedrama')
def idade_drama():
    return render_template('idadedrama.html')


@app.route('/idadeterror')
def idade_terror():
    return render_template('idadeterror.html')


@app.route('/idadecomedia')
def idade_comedia():
    return render_template('idadecomedia.html')

@app.route('/idadeacao')
def idade_acao():
    return render_template('idadeacao.html')

@app.route('/idadesuspense')
def idade_suspense():
    return  render_template('idadesuspense.html')

@app.route('/idadeanimacao')
def idade_animaçao():
    return render_template('idadeanimacao.html')

@app.route('/drama18')
def drama18():
    return render_template('drama18.html')

@app.route('/drama16')
def drama16():
    return render_template('drama16.html')

@app.route('/drama14')
def drama14():
    return render_template('drama14.html')

@app.route('/drama12')
def drama12():
    return render_template('drama12.html')

@app.route('/drama10')
def drama10():
    return render_template('drama10.html')

@app.route('/dramalivre')
def dramalivre():
    return render_template('dramalivre.html')

@app.route('/terror18')
def terror18():
    return render_template('terror18.html')

@app.route('/terror16')
def terror16():
    return render_template('terror16.html')

@app.route('/terror14')
def terror14():
    return render_template('terror14.html')

@app.route('/terror12')
def terror12():
    return render_template('terror12.html')

@app.route('/terror10')
def terror10():
    return render_template('terror10.html')

@app.route('/terrorlivre')
def terrorlivre():
    return render_template('terrorlivre.html')


@app.route('/acao18')
def ação18():
    return render_template('açao18.html')

@app.route('/acao16')
def ação16():
    return render_template('açao16.html')

@app.route('/acao14')
def ação14():
    return render_template('açao14.html')

@app.route('/acao12')
def ação12():
    return render_template('açao12.html')

@app.route('/acao10')
def ação10():
    return render_template('açao10.html')

@app.route('/acaolivre')
def acao_livre():
    return render_template('acaolivre.html')

@app.route('/18suspense')
def suspense18():
    return render_template('18suspense.html')

@app.route('/16suspense')
def suspense16():
    return render_template('16suspense.html')

@app.route('/14suspense')
def suspense14():
    return render_template('14suspense.html')

@app.route('/12suspense')
def suspense12():
    return render_template('12suspense.html')

@app.route('/10suspense')
def suspense10():
    return render_template('10suspense.html')

@app.route('/suspenselivre')
def suspense_livre():
    return render_template('suspenselivre.html')

@app.route('/animacao18')
def animacao18():
    return render_template('18.html')

@app.route('/animacao16')
def animacao16():
    return render_template('16.html')

@app.route('/animacao14')
def animacao14():
    return render_template('14.html')

@app.route('/animacao12')
def animaçao12():
    return render_template('12.html')

@app.route('/animacao10')
def animaçao10():
    return render_template('10.html')

@app.route('/animacaolivre')
def animaçao_livre():
    return render_template('Livre.html')

@app.route('/comedia18')
def comedia18():
    return render_template('18c.html')

@app.route('/comedia16')
def comedia16():
    return render_template('16c.html')

@app.route('/comedia14')
def comedia14():
    return render_template('14c.html')

@app.route('/comedia12')
def comedia12():
    return render_template('12c.html')

@app.route('/comedia10')
def comedia10():
    return render_template('10c.html')

@app.route('/comedialivre')
def comedia_livre():
    return render_template('Livrec.html')
