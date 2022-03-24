import os
import textwrap
from datetime import datetime

def html_string(nome, idade, justificativa, anos, meses, dias, exames, hipotese, cid, carater, duracao, anestesia,
                gravidade, cx1="", cx2="", cx3="", cx4="", cx5="", cx6="", cx7="", cx8="", code1="", code2="", code3="",
                code4="", code5="", code6="", code7="", code8="", qx1="", qx2="", qx3="", qx4="", qx5="", qx6="",
                qx7="", qx8="", opme1="", opme2="", opme3="", opme4="", opme5="", opme6="", forn1="", forn2="",
                forn3="", forn4="", forn5="", forn6="", qo1="", qo2="", qo3="", qo4="", qo5="", qo6=""):
    # print("pixel", get_text_size(str('Nome:_' + str(nome))))
    # field_nome = f"<u>{nome}</u>"+"_" * int(round((906 - get_text_size(str('Nome:_' + str(nome))))/10, 0))
    field_nome = str(nome)
    # 505 - field nome
    # 906 - linha completa
    # 10 - somente _
    field_idade = str(idade)

    # field_justificativa
    if len(justificativa) > 111:
        wrapper_88 = textwrap.wrap(justificativa, 111)
        first_line_justificativa = wrapper_88[0]

        if len(wrapper_88) > 1:
            remanescent_of_justificativa = justificativa[justificativa.index(wrapper_88[1]):]
            wrapper_113 = textwrap.wrap(remanescent_of_justificativa, 140)
            second_line_justificativa = wrapper_113[0]
            if len(wrapper_113) > 1:
                third_line_justificativa = wrapper_113[1]
            else:
                third_line_justificativa = " "
            if len(wrapper_113) > 2:
                forth_line_justificativa = wrapper_113[2]
            else:
                forth_line_justificativa = " "
        else:
            second_line_justificativa = " "
            third_line_justificativa = " "
            forth_line_justificativa = " "

    else:
        first_line_justificativa = justificativa
        second_line_justificativa = " "
        third_line_justificativa = " "
        forth_line_justificativa = " "

    # exames
    if len(exames) > 95:
        exames = exames[0:95]
    field_exames = exames

    # hipóteses diagnósticas
    if len(hipotese) > 64:
        hipotese = hipotese[0:64]
    field_hipotese = hipotese

    # cid
    field_cid = cid

    # carater do atendimento
    try:
        if "ambulat" in carater:
            field_ambulatorio = "X"
            field_internacao = " "
        else:
            field_ambulatorio = " "
            field_internacao = "X"
    except:
        field_ambulatorio = " "
        field_internacao = " "

    # duração da internação
    field_duracao = duracao

    # tipo de anestesia
    try:
        if "local" in anestesia:
            field_local = "X"
            field_geral = " "
        else:
            field_local = " "
            field_geral = "X"
    except:
        field_local = " "
        field_geral = " "

    # gravidade: eletiva ou urgência
    try:
        if "Urgência" in gravidade:
            field_urgencia = "X"
            field_eletiva = " "
        else:
            field_urgencia = " "
            field_eletiva = "X"
    except:
        field_urgencia = " "
        field_eletiva = " "

    dia = f'__<u>{datetime.now().strftime("%d")}</u>_'
    mes = f'__<u>{datetime.now().strftime("%m")}</u>_'
    ano = f'<u>{datetime.now().strftime("%Y")}</u>_'

    html_string = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Solicitação de Procedimento Hospitalar</title>
    </head>
    <style>
    body{
      -webkit-print-color-adjust:exact;
    }

    hr {
        top: 8px;
        border: none;
        height: 2px;
        background: black;
        margin-bottom: 10px;
        border-top: solid 1px #000 !important;
    }

    .statistics_lines {
        display:block;
        border-bottom:1px solid #4d4b4b;
        padding: 1px;
    }

    table.head {
      border:1px solid black;
      border-collapse: collapse;
    }
    table.table2 {
      border:0px solid black;
      border-collapse: collapse;
      height: 124px
      margin-bottom: 0px;
    }

    table.table2 tr { 
        line-height: 14px; 
        overflow: hidden;
        height: 30px;
        white-space: nowrap;
    }

    table.table22 tr { 
        line-height: 14px; 
        overflow: hidden;
        height: 30px;
        white-space: nowrap;
    }

    table.table22 tbody tr:nth-child(1) td:nth-child(1) {
      width: 10%;
      border:0px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table22 tbody tr:nth-child(1) td:nth-child(2) {
      width: 58%;
      border:0px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table22 tbody tr:nth-child(1) td:nth-child(3) {
      width: 8%;
      border:0px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table22 tbody tr:nth-child(1) td:nth-child(4) {
      border:0px solid black;
      border-collapse: collapse;
      text-align: center;
    }

    table.table3 tbody tr:nth-child(1) td:nth-child(2) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table3 tbody tr:nth-child(1) td:nth-child(4) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table3 tbody tr:nth-child(1) td:nth-child(6) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }

    table.table4 tbody tr:nth-child(1) td:nth-child(2) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table4 tbody tr:nth-child(1) td:nth-child(4) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table4 tbody tr:nth-child(1) td:nth-child(7) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table4 tbody tr:nth-child(1) td:nth-child(9) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }

    table.table42 tbody tr:nth-child(1) td:nth-child(2) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table42 tbody tr:nth-child(1) td:nth-child(4) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table42 tbody tr:nth-child(1) td:nth-child(7) {
      width: 39%;
      border:0px solid black;
      border-collapse: collapse;
      text-align: center;
    }

    table.table5 tbody tr:nth-child(1) td:nth-child(3) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    table.table5 tbody tr:nth-child(1) td:nth-child(5) {
      border:1px solid black;
      border-collapse: collapse;
      text-align: center;
    }
    .break { page-break-before: always; }

    </style>
    <body onload="window.print()">

    <table class="head" style="width:100%">
      <tr>
        <th bgcolor="black" style="width:5%"></th>
        <th bgcolor="black" style="width:5%"><img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/4QAWRXhpZgAATU0AKgAAAAgAAAAAAAD/2wBDAAUDBAQEAwUEBAQFBQUGBwwIBwcHBw8LCwkMEQ8SEhEPERETFhwXExQaFRERGCEYGh0dHx8fExciJCIeJBweHx7/2wBDAQUFBQcGBw4ICA4eFBEUHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eHh7/wAARCAH6AXEDASIAAhEBAxEB/8QAGwABAAMBAQEBAAAAAAAAAAAAAAcICQYFBAP/xABXEAACAQMEAQMCAgUFCQsJCAMBAgMABAUGBxESEwghIhQxFTIJFiNBURcYN3a0JDNCVVeUldLUJTQ4UlZhcXOEpdMmJzU2Q1NicoJERUdUY2eBhZPE5P/EABQBAQAAAAAAAAAAAAAAAAAAAAD/xAAUEQEAAAAAAAAAAAAAAAAAAAAA/9oADAMBAAIRAxEAPwCmVKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKV7WmNJ6q1R9R+rOms1m/puv1H4dYy3Hi7c9e3RT156txz9+D/Cg8Wldn/JPun/AJNNZ/6Cuf8AUp/JPun/AJNNZ/6Cuf8AUoOMpXtan0nqrS/0/wCs2ms1hPqe30/4jYy2/l68duvdR247Lzx9uR/GvFoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFKV6elcBmdU6istPaex02Ryl9L4re3iHyc/ckk+yqACSxICgEkgAmg8yrAbKelvXetMphsjqO0/A9I31tHfHIJdQSSzwOqsiRIrMVd1Ye7qAo5JBICNOXo99OsOlrOz1/re08ucu7ZWtcRfWMf+5jCbukpLFj5uqRsCAjR9nUgn8vT73eqfQ+gvobbTZstb39zzJKmOySC3t4vcctMquO5YeyAc8clivx7B7OifTFs1pf6Sb9V/xu9tu/905edrjy9uw+cPtA3Abgfs/bgH8w7V+OqPUlshoixkxdjnoci2Niihgx+BtTLH04UKkMgC2/VVI9hIAApX8w61RncfencPWeos5fS6s1BZYvKyygYmLJyC2it25UQFE6oyhOFJ6jv7luSxqOaDQzcL1g7X4PFrJpU3urb+TnrBFDJZxR8MvPkkmQEcqWI6I/uvB68g17OE9WGyWQxcN5d6jvcRNJ27Wd5jJ2lj4YgdjCjp7gAjhj7Ec8HkDNqlBqxoTdLa/db8TwWm87ZZ3pbH62xuLSSPyQPyjcxzIvkT36twCB2UNx2HMQbi+jTQWTscndaLv8ngso8QNhazXPmsI3UD4t2VpurcHlu7FS3IBACGieEy2VweUhymEyd7jL+Dt4rqznaGWPspU9XUgjlSQeD9iRUs7O+ozX2hdX/jOby+a1hYSWz28uOyeYnZfkQwkjLFwjhlHuVb4lx7duQHP7rbJ7i7ZWJyeq8NDBi2vvooL6G8iljnfh2UqobyBWWNmHZVPH3APtUc1qLtTuZt5vpooW7wYy5uJYu2T05kfHPJCY2QkmNh+0iDlCsgXjkrz1YFVqb6nvTJmdEX1/qnQtlNktHrE11PCJO8+LAI7KQT2kiHPIcclVVu/5e7BWylKUClKUClKlPZPYjXu6N9aTY7GTY7T0koE+auo+sCJy4ZogSDOwMbL1TkBuAxQHkBFlWA096Q95cn1+tssLhOfJz9dkVbjr4+vPgEn5+7cf9U/bryne3+2O1G2WymkLW+u0wqXuP/aXWpsqkUUvlkAjYiV/7yh7BFQNxweCWZmZo53R9ZGkdNailw+lNPzarW2leK4vRerbWzEdeDCwSQyryXBbhR8QVLqwNB8W1/ov0vipor7X+cm1FL4kLY+0VrW2VyjB1aQN5JFDFSrL4j8PcEHqPav/AEYbT3N9cXEOU1bZxSys6W8N7CY4QTyEUvCzFR9h2ZjwPck+9V/1/wCrvdTN6ie80teQ6VxYiVI7COCC7bkfmd5ZYuWYkn7BQAFHHPLNHP8ALXu5+OfjH8o+pvqfqfqen4hJ9P37duPBz4unP/s+vTj2449qC0253otwWUyl1kdB6i/V+E237HFXUD3MXnCkD9uZO6IxC88rIVJYjkcKK87i+m3drRFjk8pfYGHI4fGxCafIY66SWPpwCziMlZuq8nsTGAArN+UdqkDbX1ma3wVjd2+tMRDrCWSUPbXAmjsJIRxwyERxFXX2BHxBBLclgQFmzZ31b6H1plPwjU1n+pl6/doZry9SSydVUEBpyE6OfnwGUL8QOxZgtBnnStJd2di9st6NMR5fTNxhcZfz3L3MOoMNBFMl0zPxN5vGVE/LBvct2Vxzz+dWoputtLr3bK+MOq8FNBaNL44MjD+1tJzy4XrKPYMwjZgjdX6+5UUHC0pSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgVcz0GbNW01vdbh6z0xzNFc276da9jmRk4jLtcrGwCSIwliMcny4aMlepAJrz6c9s5N190bLTDzzW2OSJ7vJ3EPTyRW6cA9Qx/MzsiAgN1L9ipCkVf8A9R+r8NtjsVlniebEtNYvh8ImNj8bQ3DwusIj68CJUClueR1Efx5bqpCM/V56jZNDTXGhdC3U1vq2GWB7y8kskkhtYWQydE8h4aUgxH8jL1kb3Dj40Gr97+7ur++uL6+uZrq7uZWmnnmkLySux5Z2Y+7MSSST7kmvwoFKUoFKUoFKUoOg0BrTVGgtRJqDSOYmxWRWJoTLGquro33R0cFXX2B4YEAqpHuARo/sBuzpve7Q95DJY9r+0tobbPWFzaD6d2miIboCzh4XZZVAY9uFPYDkE5gVI3ps15HtxvLgtSXk00eL8ptckI5XVTbygozOFDF1QlZenB5Ma8cHggPa9VG0t1tnuTkxisFk7bR9xLG2LvJeZYeZI+zQiX/jK6ygI579UBPbnsYfrUXdTSGl/UHs1b2uKz0JsbyWK/xeVijaVYXQlWJj7Jy3QyxlHIKljyAy8DMG/tpLK+uLOZoWlglaJ2hmSaMlTwSroSrr7ezKSCPcEig/ClKk304bUX+7W4dvhul7Bg7b9tl7+3RT9PFwSqgt7B5GXov5iPk3VgjCg6D0rbG5HdjUQyt4YYNK4m+hGSMyyhrwe7tBCVABbhVVz3UoJVYc+wN69Wak2+2J20s2u4fwfAWf9x2FpZ27yNLL0eQRrxzy79HJeRgCxJZuSTX47la80Rsft1aJdzQ2sVrYm0wWLMsjSXRgh/ZwhuHYL7IplYEKWXseSOc090ta5XcTXeR1jm7eyt7/ACHi8sdmjLEvjiSIdQzMfyoOeSffn/ooOt3x311vuxNPZ5i4htdPC+F3ZYmKGMrbFUZF5l6iR26u3JJ4JYkKo4AiylKBSlKBSlKCefTx6ltUbYw47TWTghy+j4JeGtRCq3NqjPI7tC469mLydisnYHqFBTnkXT/83HqL2g/xjhb7/oS7x10o/wD58cydv+dWVv8ADjf5ZZ1Yb0Zb2Wu22orrA6uzM1no+8imnCx2YlWK9PiAlcopl6lIinC9hyykqPdgEM7i6QzOgta5PSOoEhXI46UJKYZO8bhlDo6n/isjKw5AIB4IB5A5+tGfWHttitz9rItY2eovD+rWNvMrZyW6LcW99A0AlKghh+bxR9ZASAC3xbkEZzUClKUClKUClKUClKUClKUClKUClKUClKUClKUClKUF3/0b+kMMulc9r4pM2ae+kw6sZP2cduqQTEBR/hM7Dknn2ReOPl2iz157lWGtNy7XTOIHey0r9RazTNCyM94zgTqCT7ovijUHqPkJCOylTVmfQpi7DH+m3B3dnB4psnc3d1eN3Y+SUTvCG4J4H7OGNeBwPjz9ySaG77f0368/rJkf7TJQcZSlKBSlKBSlKBSlKBSlKDRL0Davw2b2PttLWbzDKaclkS/jkj4XieeaWJ0b7MpBYfuIKNyOCpapvq42zw21u7Jwunp5mxeQsUyVvBL8mtQ8kiGEOSS6gxkgn34IB7EFm7n9HF/Tfmf6tz/2m2r0/wBJLhLqDcXS+o3khNpfYhrKJAT5A8EzO5I446kXKccEnkNyBwOQrbobTOV1lq/FaWwkPlv8ncpbxcqxVOT7yP1BIRV5ZiAeFUn91aS6TwWjfTVsbeS3F1e3Fhj/AO7MldCMtLeXUnSPlI+eE7MI0VeQqjjs35nPJeiPaK10LoKHWd5cw3ua1RYwXKskY62lq6+RIlYjt2bsrSe4UlUAB6dmg31v73R6wy0GitFakhvdKwRB8i1ojqtzdrK46M54EsShI3XpyhLduW6r1CLPURulndytcX31ud/FcBjsle/gP9yJD47WSUdfsiueUSP8/LDj+PNRlXQaA0XqjXuok0/pHDzZXItE0xijZUVEX7u7uQqL7gcsQCWUD3IBulst6Q9G2emMfkNyrK9yOfntm+sxy5EraW7s/ZephCOXVAqt82TsX45HU0FM8Jt7r7OYuHKYTQ+psnYT9vFdWeKnmik6sVPV1Ug8MCDwfuCKk3b30q7uavxbZGXG2WmofbxLnJJIJZfkyniJUd04K/4aryGUr2B5q7+v98dq9B6ifT2qdWw2WUjiWWS3jtZ7how3uocxIwViOD1JB4KnjhgTHOE9ZO0eQykNnd22psRDJ27Xl5YxtFHwpI7CGR39yABwp9yOeByQFQNbbD7p6X1Pd4L9T81m/pun93YjGXNxaS9kV/hJ4x247dT7ezAj91cZqfSeqtL/AE/6zaazWE+p7fT/AIjYy2/l68duvdR247Lzx9uR/Gr8ab9Yez+Vvnt75tQYGJYi4uL/AB4eNjyB0AgeRux5J91A4U+/PAMm293t1vjttcw29zDqPTF9KIbhI5JYG7xSK4RwOkkbBlRuDwSCp91YchlBSrZ+pX0pZXG5STUG02F+pwa2ytcYlLxpbqGRVcu0Sye7oVVPiHeQu5CrxwBUygUpSg0y9G2uv152Qxv+5f4f+r/iwX++PL9R9PbQftfyr17d/wAvvxx9zVGvVHpbBaL321FpnTNj9BibP6X6e38rydO9rE7fJyWPLMx9yfv/AAqbP0dW4lrjczlttsndTK2WlF7iIhADGZkjb6gFwOwZo44yO3x4ib3DEBum/SQaQwzaVwOvgky5pL6PDswk/ZyW7JPMAVP+ErqeCOPZ255+PUKQUpSgUpSgUpSgUpSgUpSgUpSgUpSgUr2tDaZyustX4rS2Eh8t/k7lLeLlWKpyfeR+oJCKvLMQDwqk/uq3+03ousLbyXe5+a+umjuUa3ssNcMtvJEvuwmkeMOex+PCdCoHIYlviFJqVqZpjYHZrTv1H4ft7hZvqOvf8RRr/jrzx1+oL9PzHnrxz7c88Dj07fbLaG5muYbfb3Q00trKIbhI8Nas0LlFcI4CfFujo3B9+GU/YigygpWn+b9N2yWYyk2Ru9A2UU03Xstncz2sQ4UKOsUMiovsBzwo5PJPJJNQZvL6Mv8AfOW2tyv/ABpPwXJSf/O3SGf/APxoqyD+JaWgnP0fZS/zHpt0dd5GfzzR20tqrdFXiKCeSGJeFAHxjjRefueOTySTWee+39N+vP6yZH+0yVoz6XNLZ3RexOndM6msfoMtZ/VfUW/lSTp3upXX5ISp5VlPsT9/41nNvt/Tfrz+smR/tMlBxlKUoFKUoFKUoFKUoFKUoLM/o4v6b8z/AFbn/tNtVrNabV3WpvUBpDcS8zEM2F09YzKuIuITIv1RLdJkBPVW+asX47A20XHPPMdWv0b9pdPvDnr5LaZrSHT8kMs4jJjR3uICiFvsGYRuQD7kI3H2NWl9SW8GM2i0U96fDcahvonGGsZkk8dw6tGrszIpAVBKHKllLAdQQTyAjn1ub23+hsHb6Q0ZlbKLOZPyx5G4t7pTd4yILGwAQe8byLLyrnghVYqOSGWoGxe1GpN29XrhMIn09lB1kyWSkQtFZREn3P27O3BCoCCxB9woZlaY0zuPvluHcT2sN7m8tf3KtkcnOpFvbdgeGmcDrEgVGCqB9k6opIC1oxiMdt9sLtQVVvwjTmM6Nd3bxPNLNLI6R+WXxqWd2YoOQvAHAAVVAANu9HaH2X28gt1fC4iG1toY8rmZwlr9XKDx5ZpHYn5SSN1VmIXv1X24FVA9QnquzusfFitupc1pXEpz9Rc+ZI7u758bL7oC0HRlcfCQ91b5cD41HPqO3kzO7+qo7i6jhtsLjJbhMPbpB45FhkfkPKezcylFiDcN1BT4gckmLKD09VZ/M6p1Fe6h1DkZsjlL6Xy3FxKfk5+wAA9lUAABQAFAAAAAFeZSlArptvdf6y2/yjZHR2ob3ETSceVYmDRTcKyjyRMCknAduOynqTyOD71zNKDRL0z+pe13W1EdJ5rBQ4PNLYieGWO8Dw3rpx5VRGAZG9+6oDIequS3w5aJvXrs1JYZZt0dMYqGLFzRc6gERSNYrgyqiTkF+WaUygEInsYy7clyaqngspf4POWGbxc/09/j7mO6tZeit45Y2DI3DAg8MAeCCP41p/t1rHTe/uzF/NbJe2FtlLa4xOUtwR5bSV4usiI5Xq/CyBlfgghhyAeygMs6V1u8Gh7rbjcnM6LvL6G/lxsqBbmJSqyo8ayIxU/lbo68ryQDyAWA5PJUEgenDKX+H370Pd46fwTSZu2tWborcxTyCGVeGBHyjkdefuOeRwQDVv8A9I7/AEIYb+skH9muapnsT/TfoP8ArJjv7THV7PXnhLXK+nPJ31xJMsuGvrS9txGQFZ2lFuQ/IPK9J3PtweQvvxyCGcFKUoFKUoFKUoFKUoFKUoFKUoFd1tHtbq7cnUWNscLhsmcXc3y2t3lo7NntrMDhpGdyVTsqHt0LAtyoHuw54ywtpL2+t7OFoVlnlWJGmmSGMFjwCzuQqL7+7MQAPckCtONndJYL0/7G+DUmXsoEtO+QzeRBfxPO/C/ANyTwojiUKAXKghAz8UHQYyLQWyG11hjLnLw4bT2KiaOKa/ueZJnPeV+P3ySufI/RByTyFUAACoG7nrE1dqGHJYfROMh05i7mJoEvZHZ8iB3P7RGUhIWZOo4AcoSxV+epEceo/evO7tanuFW6vbXSdvc+TFYqUoPHwgTySdAOztwzcMX6eRlVuCSYmoPam1ZqqfKZDKTalzUt/k7Y2l/dPfSmW7gKqpilcty6FVUdWJHCgcewr4sJlsrg8pDlMJk73GX8HbxXVnO0MsfZSp6upBHKkg8H7Eivir09N6ez+pb57HTmDyeZu44jM8FhaPcSKgIBcqgJC8so5+3JH8aDoP5WN0/8pes/9O3P+vU87fetTV1lfWdvrfT2My2OWJIp7iwVre7JBUNMQWMbt1DnoFjBYjhkA4rjNN+knenK3z299h8ZgYliLi4v8lE8bHkDoBAZG7Hkn3UDhT788A8Nm9lN3MPlJsdd7camlmh69ms8fJdRHlQw6ywhkb2I54Y8HkHggig0y0buDofWXjXS2rcLl5pLYXX01teI1wkR6/J4ue6cFlBDKCCQDwfaof8AUn6acBuHNnda4efJ22sJbEGGCOZDbXk0SAIrrJx1Z0VY+wdVXhWIPDdqgbbPrTZDcHC7iaj281BHaWMs0KR39rNYxzPLbyxhBK8ZAbhmbjgkhT/0jSzPZ36bQ9/qbBWv6weLGyX1jb2Unf6/iIvGkbIG57+wUqG57DgGgyz3H2s3B278Lax0ve4yGfqI7nlJrdmbtwnljLJ34Rj07duBzxxwa4ytOdtdxtvN9bG70/nNMQpmsPKJMhp3UFlHLJbTKOjyIrg9lR2eMtwrKT8lTuoMS7tei/GZK+uMnttnIcIrRRiLEX6ySwBwQHYXHZpFUr8upVz259wpAUKQUqWdzvT5ubo3V91hLTS+a1JZL+0tclisbLPFPESepPQN439iGQnkEexZSrNGeVxOVxP0n4pjL2w+stku7X6mBo/PA/PSVOwHZG4PDDkHg8Gg+KlKUClKlPQHp+3Y1fqJMOmkcnglMTSve5uzmtLaML+4sycsxJACqGPvzx1DEBFlWG9Ofpk1Fr6+sszrOyyeD0fdWL3VvdwyQrPdHkLGqqxLRq3JcO0ZDKvt+dWqyewvph0bobBtJrHG4XVufuOTJPc2Zkt7dGWPmFI5CyN1dGIl6K5DEcKORXTX29egdPbl4TaXCY+9yd/P47SKPAwwTWuP6u0RilCyAxeJYyzqF+CDnj91BI2k8Ja6a0ridOWMk0lpirGGygeYgyMkSBFLEAAtwo54AHP7hVBvU5qO53737x2mduUvcr9DbTY+2t5LqFLeeeKSZ5p4GMhjKPGiEOSpYIvt7LVwPUdq3WWltD2cG32I/E9UZ7JJiccOA307vFLIZup+J6rEx+ZCL+ZuVUg+L6fNlNN7GYPM5K9y9lkb+btJc5u4tha/T2aqrGI9pHCIGVnZuRz8e3PReA9PaPbXQWw2irmYZKG1aWKAZnNZG68Mdw6swRiHbxxL2lKqo9+CoJdvc0T9Um7f8rm4aZTHre2+AsbZLfG2tyOjryA0sjoHdA7OSOVI5RIwfcV1vrK3yk3H1E+j8GIV0rhb5ikyskjX9wnaPzh1JAi4ZwgU/IN2bnlVSLNsdr9cbjZS1tNL4C9uLae5+mkyTwOtlbMFDN5ZuCq9VIbj3Y8gAEkAhxlK0f2O9MOi9v7HJpqNMZre7vpYykuSw8PjtkQHhY0cyEMSzFm7cEBBwOvJ7PUmiNjNNWKX2o9Ibc4a0klEKT3+NsreNnIJCBnUAtwrHj78A/woMraVqxhP5F9XYuHR2E/k/wA/YWPa7iw9n9HcxW/yIMqwLyF+Up5YAe8h9/l78nvL6atvNe6dis8LisZo7KW0veC/xeNjRSDx3SWJOglUge3JBUgEHgsrBmnSut3a2/z+2WtbjSmo1ha7hijmSe3DmCdHUEPGzqpZQeyE8cdkYfurkqBVpvQJullcRrO02q/DbKbE5u5urz6nlluIZ1tg3PPJVk62/XrwDy/PbgdTVmpm9Ev/AAndI/8Abf7FPQSz+kS21sMfeY7dHHHxTZO5XH5WN5mPklEP7CRFI4H7OF1b5AfGPheS5NQKv/8ApHf6EMN/WSD+zXNUAoOz2J/pv0H/AFkx39pjq7/6QTN3WK9P7WNvHC0WZy9tZXBkBLKih7gFOCOG7wIPfkcFvbngilvpwxd/mN+9D2mOg880ebtrpl7qvEUEgmlbliB8Y43bj7njgckgVb/9I7/Qhhv6yQf2a5oKAUpSgUpSgUpSgUpSgUpSgUpSgnn0KaQw2rd9YnzSTSLg7FsxaJHJ0VriKaFYy/HuVUyduARyVXnleVM5/pAN1cjpvDWe3OEuYY5c9YyS5VgsqzxW/kQRiN1YL1k6To6ntyoIIAYc9b6D9LYLE7E43U2PsfDls95fxK48rt5/BdXCRfEkqvVSR8QOf38mqjesHXF1rffXNG4sYbOLAyyYO3WNizSJbzSgyOT/AITOzngAAAqPcgsQh+lKu/6AdorWyw0O7uTuYbq7yEU9tirYRhhaoshjklLMORKxjZR14AQtyW7kIHx+n70gWosfxrd+CY3ZlYQ4O3vAI1QBl7TyxHlmJIZVjcABR2Ldii2F3C3o2v0DlFxeqtX2VlfnntaxRyXMsXxVh5EhVjHyrqR3A7A8jng1DPqr9TsOkLi+0Pt/P5tRxcLdZaNo3ix0qyKWiCOjLK5UOrD2CFh7lgyrRrN5bK5zKTZTN5O9yd/P18t1eTtNLJ1UKOzsSTwoAHJ+wAoL83/rP2ntr64t4cXq28iilZEuIbKERzAHgOoeZWCn7jsqng+4B9q+zTfrD2fyt89vfNqDAxLEXFxf48PGx5A6AQPI3Y8k+6gcKffngHO2lBqkl3tLv7oqWxS5xmq8OsqTSwCR4p7ZwzBHK/GaBj1cAnqWXtxyrHn7dlNr8BtNpW505py8yd1aXN896738iPIHZI0IBREHXiNf3c8k+9ZZ6b1Dn9NXz32nM5k8NdyRGF57C7e3kZCQShZCCV5VTx9uQP4VOezXqw17omGWx1OJta47xcW63t547mB+5Yt9QUdpFPYgq/YjhOpUAghOfq89OUmuZrjXWhbWa41bNLAl5ZyXqRw3UKoY+6eQcLKAIh+dV6xt7Fz8oG2r9VuvtC6Ywul/wvC5jE4viPtd+f6uSDuW8Yl8hVeqnoh6EKqqOpA4N0tpd5NF7g6Kt9QQ5fGYy7FjJeZHGXGRhM+PSJisryANysQI5EjBQVZSQvPA5/1CenrSu7fiyH1P6v5+Ln/dG1s4n+p58a/3QOFeXqkfVPmvXsfuPag8zSvqy2cyenbK+zWdmwORli5ucfLY3M7W7/YqJI4irr7chhwSCOQp5Udne3uz+9+nV07LldP6rtJoo8gLKK9AuYQOOJCqMJoWHcKfykdyrfmINDd2vT1uHorWtxg8Rp3UGqccsUcttlLDESPHMGUdgVjMnRlfsvVm54UNxwwqLM3icrg8pNi83jL3GX8HXy2t5A0MsfZQw7IwBHKkEcj7EGg0fv8A0q7HXNjcW8OkZrOWWJkS4hyt0ZISRwHUPIylh9x2VhyPcEe1fhhPSfslj8XDZ3enL3LzR9u15eZOdZZOWJHYQuiewIA4UewHPJ5Job/Kxun/AJS9Z/6duf8AXp/Kxun/AJS9Z/6duf8AXoNH7K22f2K060UTaf0haTRSSkyzAXN6IuXIBcma4ZfIeF+ZHcKo9wK5LPeqzZizwd/d4vVH4nfwW0klrZfQXcP1MqqSkXkaHhOzAL2PsOeTWen/AJVa51P/APfWps/e/wDW3l3cdE/+p26on/Pwq/wFTNsj6WNca9+uudSC90RYW3EcT5HGubi4l9jwsLMh6BT7uTxzwFDfLqHsw+oHfHerKY/bjTj4XT9/lbkcXeKM1pKEjVpH5maVyiBVLt0HchOo55KtbPYDZjTezuDvLTD3d7kL/JeFsje3LAeVo1IASMeyIGaRgPk3zILNwOPZ2x2v0Ptzi7W00vgLK3uYLb6aTJPAjXtypYM3lm4DN2YBuPZRwAAAABz+8G+Oi9BaSzOTs83p/PZrGSpC2DizUMdy7+ZY3QqOzKycsxHUkdDzx9wHW62ymk9F2d3uBqef6OGytktZb10lm8ETzKOqRqGK95Gj7FF5bpH25Ea9aDeqjf7M7kaiyentPZeaPQaSxrb262/ha8MfuZZSfmylySqEgcLGSgcE1z+8W52uN9td+Cwss09lL0OO01ZyvdrE0cR7OqIi+R/eVi5TsFYrz1UVY309+kiHT2UxOrNxLyyydyttI0unXso57eOV1KgSyMWWXqrE8KoAcAhmC8sEc+kz002u4OGi1zreeaPT0kpGPsbWYLJemOTrI0rDkpFyjp1HDk8kFAFL24u8ttfsXoSxxd3k7LTWDtvJ9FayzyTyv2l7SeNCXll4eUE8Buobk8AVw27/AKjNvNsdK4lNHy6f1VK0q2sOLxGUjSO1t0Q/LtEkioq/s1VCF5DHr7KeKDbha/1luBlFyOsdQ3uXmj58SysFih5VVPjiUBI+Qi89VHYjk8n3oJa3r9UuuNeYvM6XxqWWH05eXMixyW8Dx3s1n2brFM3kdR2Ur3Ccc8FeepINf6UoFTn6ZPUBqTbTOYvAZTI/VaIkuSl1azqW+iWVl7zxMqlx1PLmMcq3L8KGbuIMpQai7laH0F6hNrrSaG+huIJ4jcYXNWy9pLVz7E8HgleV6yRNweV4PV1UrmbqzCXWmtVZbTl9JDJd4q+msp3hJMbPE5RipIBK8qeOQDx+4Vcz9H3updZXHLtLcYeFYsNY3OQt8hHMQzI1whMbxkHlu87nuGA4Cjrzyx4z9I3pDDYjWun9XWKTR5HUMU6ZAGTtG5tlgSNwD+VujhTweCEU8A9iwVTrs9if6b9B/wBZMd/aY64ypT9JeEtc/wCozRljeSTRxRXzXqmIgN3tonuEB5B+JeJQf38E8EH3AWs/SO/0IYb+skH9muaoBV//ANI7/Qhhv6yQf2a5qgFBaD9Hhoe1zu5OS1pcX00Uul4kFvbRqOsz3Uc8ZZ2P+CqK/wAQOSWU8gKQ3Z/pINcWoscDtsljMbsyx5yW6LARqgE8CRgfdmJLkk8ABV47dj1+z9GphLqDSustRvJCbS+vrayiQE+QPAju5I446kXKccEnkNyBwOYN9cU0cvqX1KiWkMDQxWaO8ZctOfpYm7v2YgNwwX4hRwi+3bsxCEqUpQKUpQKUpQKUpQKUpQKUpQac+jK0urL00aPhvLaa2laK5mVJYyjFJLqZ0cA/4LIysD9iGBHsazTz2Uv85nL/ADeUn+ov8hcyXV1L0VfJLIxZ24UADliTwAB/CtJfRL/wYtI/9t/ts9Zm0HTbT4uwzm6eksJlIPqLDIZuytbqLuy+SKSdFdeVII5Ukcgg/wAK0m3SzFhsfsDkclpDAWSW2BtoobCxLMsStJMkYZyPk/DSd25PZzzywLFqqZ+jotsVcbz5V7vH+e/tsJLPZXDMpW3/AGsSSEKVJ7ssgAcMvC+RSG7/AB6D9JBq/MtqrA6BDwrhUsY8wyiP9pJcM88IJY/4Kop4A493bnn49Qqbf3d1f31xfX1zNdXdzK00880heSV2PLOzH3ZiSSSfck1+FKm30pbGybvaivJ80cnYaVx8TCe9tVRWluDx0gRnBAbhu7EK3AAB6+RTQc/sjsfrjdz66bTcVlaWFjwst/kZHjt2lPB8SlUYs/U9iAOFHHYjsoa1mifRpoK107hRq6/yeQzVvKZ8i1lc+K2uSeh+n4K9vEvUgMpR27uSV5VUkzfHdXSOzegp4ornGQZiGxEWEwkSqWJ6skJMKspW3UoeW+IAQqp7dVNM9f8Aqw3Y1bp18Kk+M06skqu93hEmt7lgvv0EjSsVUngnrwTxxz1LAhaDU/pD2ay/0/4fZZrT/i7d/wAOyLP5ueOO31Al444PHXr+Y88+3EJaq9E+tE1FejS2pdPzYXy82bZKeaO5CH36yCOFlLD3HYHhuOeF56iJtAeoHdjSGokzCauyedURNE9lm7ya7tpA37yrPyrAgEMpU+3HPUsDM2H9cGfivsg+X0DjLu0kl5sIrW/e3kgTlvjK7LIJW4KjsqxjkE8e4ACtm52hdSbc6vutL6osvp72D5RyIS0VzESessTcDsjcH39iCCpAYECYNo/Vbr/TGosbFqm5hzOlYYltZMdbY+2tWt4RwFaDxIgDIAOEPxI5X48hltztjvbtlujpC1W7yuFsL3Kf3Bdafyt1F5XlcBWhCPx50fsApCkOG4IDdlHDX/ow2nub64uIcpq2zillZ0t4b2ExwgnkIpeFmKj7DszHge5J96DrNsfUxtTrzKWuHtMne4fLXlz9Na2WVtvG0zdQV4kQvEOxJVQXDFhwByV57Pcfazb7cTwtrHS9lk5oOojueXhuFVe3CeWMq/Tl2PTt15PPHPBrOfcTYbdbQvnmzGkb24sIfMxv8cPqrfxRe7SsY+TEnX5AyhDxz7DhgOM0xqzVWl/qP1Z1LmsJ9T1+o/Dr6W38vXnr26MO3HZuOftyf40GjH81zYn/AJDf97Xv/jU/mubE/wDIb/va9/8AGqgH8rG6f+UvWf8Ap25/16fysbp/5S9Z/wCnbn/XoNLNtdotutuL67vtGaZhxl3eRCGaczyzyFAeegaV2KqTwSF4BKrzz1HHM7i+pLaXRF9k8XfZ6bI5jGyiGfH461eWTvyAyCQhYey8nsDICCrL+Ydazg1PqzVWqPp/1m1Lms39N2+n/Eb6W48Xbjt17sevPVeePvwP4V+2gNF6o17qJNP6Rw82VyLRNMYo2VFRF+7u7kKi+4HLEAllA9yAQsBu16w9b5XM3Fvt20OBwqyxva3Fxj43v2HjAdJA7yRdS5YjqoPCr7/mBh/ZHaTVW7mcvsXplrK3+hthcXF1fGVLdeWCrGXRH4duWIBA5COf3VMGzXpA1hmNRSnc2CbTeFgi5C2t5bzXN055AVChkVFX7szDk+wAPJZLWay1ntxsbt5JjILnC438IxplxmAW7CXFz7sEVU+Uh7ychpSre5d2J4Y0HxenDZTBbS6Yt2a1srrVlxbePK5WIOfJy5fxx9yeqLyq8qE7+NWZeQAK5+pL1YfrJi8jo7bq08eHvraazv8AJ31vxLOjN1IgQnhEaMH5OO5EnssbKCYf3l3g17vTqKKxu/N+HPfc4nA2Sd1jd+ERfioaeU/YM3J5d+gUN1qYPTp6Sr/Ncag3Xtr3FWA8UlniI5VS4uQerkzkcmJOvKFPjLyW5MfUdgqzhMTlc5lIcXhMZe5O/n7eK1s4Gmlk6qWPVFBJ4UEngfYE1Yz+ZVun/j/Rn+eXP+z1b/N6/wBo9rsXNh7vUOmdOw4zr2xNm0Ylg8jBh1tYQX+RkDnhPsxY+3JqvV/65bVL64Sx20mntFlYQSzZoRSOnPxZkELBWI4JUMwB9uT96CJdf+k/djSWnXzSQYzUSxyqj2mEea4uVDe3cRtEpZQeAevJHPPHUMRA1X5219ZmiM7fXdvrTETaPijiD21wJpL+OY88MhEcQZG9wR8SCA3JUgBpM3h240Xv5oKyRM3DJFDLJPi8xjHhuFV+rRsvf37xdwC6KyljEo7ArQZdUroNf6L1RoLUT6f1dh5sVkViWYRSMrq6N9nR0JV19iOVJAKsD7ggc/QTb6Hbu6tvUvpqG3uZoYrqK8huEjkKrMgtZXCOB+Ze6I3B9uVU/cCrGfpD9D3Wd22xutLe+hii0vK4uLaRT2mS6kgjDIw/wldU+JHBDMeQVAakGhPx39eMD+q3/p/8St/wv8n++vKvi/vnw/P1/N8f4+1aP+s20ur300awhs7aa5lWK2mZIoy7BI7qF3cgf4KorMT9gFJPsKDMapm9Ev8AwndI/wDbf7FPUM1cz9G5or/1j3GmuP44S2hR/wDqppmdSv8A1AUhv/ecj8poOm/SR5Swh2s05hJJ+t/d5sXUEXRvnFDBKsjc8cDhp4hwTye3tzweKG1Yz9IDrG/zm9R0rInisNNW0ccC8qfJLcRxzSS89QRypiTqSw/ZcjjsRXAemTbn+U7d/F4C5j74m35vst8uObWMr2T2dW+bMkfKnsvk7ccKaC8uzuCsNmPTD+KW2IvfrbfCPqDKWl5K0csl59KJJI25X9lx0EYHX4hRyGbsTnBqzN3WpdVZbUd9HDHd5W+mvZ0hBEavK5dgoJJC8seOSTx+81oZ63NzI9B7TTYO3ghuMpqqKfGxJL36x25j6zzDgcFlEiKAWHvIG+QVlOcFApSlApSlApSlApSlApSlApSlBpl6Jf8AgxaR/wC2/wBtnrNrPY/8Jzl/i/rbK/8Ao7mS3+qspfJbz9GK+SN+B2RuOVPA5BBrSX0S/wDBi0j/ANt/ts9UA32/pv15/WTI/wBpkoLGfo0cXYTZzW+bkg7X9pbWdrBL3b4RTNK0i8c8HloIjyRyOvtxyeeZ/SO/034b+rcH9pua6b9GjlLCHOa3wkk/W/u7azuoIujfOKFpVkbnjgcNPEOCeT29ueDxzP6R3+m/Df1bg/tNzQVmrVj066Ov9A7K6Z0rlH7X9pbNJdLwv7KWaR5ni5VmDdGkKdgeG68jjnis2tif6b9B/wBZMd/aY6vN6+87+Eenm7x/0vm/G8la2PfydfD1Y3Hfjg9v979ePb8/PPtwQoZudrrUm42r7rVGqL36i9n+McaArFbRAnrFEvJ6ovJ9vckksSWJJ5mld1tHtPrfdO+ubfSGNhuYrOWBL64muo4o7USlgrsGPZl+Dk9FY8L9iSAQ4WvTuNPZ+207bajuMHk4cLdSmG3yMlo620zjsCiSkdWb4P7A8/Fv4GtMtA6A209PmisxlbW6msLHxLLlcpkbkySTBGfxgqoC9h5SirGgLEqOGYjnzP50exP/AC5/7pvf/BoM1LC7urC+t76xuZrW7tpVmgnhkKSROp5V1Ye6sCAQR7girGbS+rbX+K1rb3G4mYmz2nGikS6t7fG2yTqepKPGUEfyDhQezEdWb256kXMw+f203p0VkLDH5HGanwt1F4r60JKyRgswUyRt1kibtGWRiFPKhlPsDUJbpejbRuQxeRvNv7m9xGYk8X0VneXxbHx8Mgk7ExvN7qHI+R+RH2X2ASPtBvpt5vVfZbS2MxuTWVLFpbizy9nH47q3YiOQfF3UqO6hlbjkOOAR249nUmxWz+fsUs77bvT8MSSiUNYWospOQCOC8HRivufiTxzweOQOM7d6NodZbS5S1s9VQWTQ33f6K8s7gSRXHRUMnUHh16mRQe6ryeeOR71zOjdV6k0bnI83pbNXuIv4+B5baQr3UMrdHH2dCyqSjAqeByDQXM1t6KcFltT3eQ0zq/8AVvEy9Pp8b+Gvd+DhFDftXuAzdmDN7/btx9hXi/zGP/3R/wC4P/8AorjP56u6f+INGf5nc/7RT+erun/iDRn+Z3P+0UEwba+jPRGCvru41pl5tYRSRBLa3EMlhHCeeWcmOUs7ewA+QABbkMSCss3+mdp9pNK3GsYdHafxUWnrFnS8hsoVuyAnQIsz8M8snPQdn5dn4JJaqTa/9WG7GrdOvhUnxmnVklV3u8Ik1vcsF9+gkaViqk8E9eCeOOepYGBqC428vrLW/wBOxWO1dhk8VkZZebjIZS2gLQIOCFijDSKzN7gs/soB4BLBkrnNfa93v3Rxttk8lNmdQ5WWKyhllj4jhQfv6RLxHEg7SN1XgDu5BJJPs7KbDa93ZsbnJ6cTGWuLtpXge+v7rpGZlEbGIKgeTt1kVuevXgH5c+1Xy210PoL097XXc019DbwQRC4zWauV6yXTj2B4HJC8t1jiXk8twOzsxYPG9Ofp50vtZY2WXvoYctrMRP58kSxjgLgBo4EPsqgAr5CO7Bn91VugjL1OeqxcNNNpTau7hmyMcqG4zyGC5tghRHC2/BdZGPYozOOF6sACSGWOfVp6kJtd/iOhNHSWUmjZPp2kvvBILi+ZeJCOJApjQSdRx17Exc9urFarNQe1rbVOd1pqe71Nqa++vy150+ouPEkffoiovxQBRwqqPYD7fxrxaUoFWg9Eu9mTwWssRt3qXMzfqxdRPZYm1js4ysN7NOroXdV8nVmaRfcsAZF5AUcrV+vtwWUv8HnLDN4uf6e/x9zHdWsvRW8csbBkbhgQeGAPBBH8aC7P6QzbWbL4Cy3MsDZRfgdt9LlDLNIJZonnjW3WNACnxeWUkkqeG/wuABRmtRfVphLrP+nPWdjZyQxyxWK3rGUkL0tpUuHA4B+RSJgP3ckckD3GXVBM3otwWdzXqG0/Ngrr6P8AC/JfX1x40k62oXpInVyOfJ5BFyvLL5e4HxqzP6RLVP4TtBjtM2994bnPZJfLb+Lt57WAd3+RBC9ZTbH2IY/u5Haog/Rv2l0+8OevktpmtIdPyQyziMmNHe4gKIW+wZhG5APuQjcfY11n6TT/APD7/wDsv/8AVoKZ1pz6ZNuLrZXaa+xmqc3jJJWvp8peXETlLa1TxonvJJ15UJCHLEKB2I+y9jnntTt3qjc3VQ05pS1hnu1i887zTrFHBD3RGlYk8lVMi8hQzcfZTWiXqz1nitI7G6niu7mya/yuNmsbKylu1iluPN1gkeNTyX8azByAPsPcjnkBn1v9q+PXm8uqNU27wyWl3fFLOSKN41kt4gIoXKv8gzRxoTzx7k+w+wsz+jf0Paixz25L30xuzLJg4rUKBGqAQTvIT92YkoABwAFbnt2HWllac7Pwx7H+mjDJuNdw4xcRE75B4g9wsBuLpmRD41JZgZkU9QRzzwSvyoK2fpEta4rOa7xGjrS3vUv9Mef62SVFEUn1MVtLH4yGJPCg88hff7c/eqs1027GUsM5unq3N4uf6iwyGbvbq1l6MvkikndkbhgCOVIPBAP8a5mgUpSgUpSgUpSgUpSgUpSgUpSguN+ja1fIt9qjQM7zNE8S5i0URp44ypWGclvzdm7W/A9xwjfY/mj/APSCYS1xXqAa+t5JmlzOItr24EhBVXUvbgJwBwvSBD78nkt78cAfj6DNU4LS+98n47ffSfi+NOLsf2Tv5bqW5t/HH8AevPU/JuFHHuRU2fpG9IZnL6K0/q6xSGTHaelnTIAydZEFy0CRuAfzL3QKeDyC6ngjsVCAPRTri10TvrjxeWM11FqCIYNWiYBoHnmiKSEH8y90UEcggMSOSOps/wDpAdHWGc2VOqpH8V/pq5jkgbhj5IriSOGSLjsAOWMT9iGP7LgcdiapBsxcx2W8Oi7yZZmig1BYSusMLzSELcISFRAWdvb2VQST7AE1pL6l9IZnXmx+pNLaeSGTKXcUL28csnjWQxTxylAx9gzCMgc8DkjkgckBnBsT/TfoP+smO/tMdXy9c2mf1i9POVuI4b2a5wlzBk4I7Ze3PVvFIXHBPRYpZXJHHHQEngEHOG/tLqwvrixvraa1u7aVoZ4JoykkTqeGRlPurAggg+4IrUvbq+td2fTvjHyWSmul1Dp82WTuoYxDIZmiMFyVBXqrCQSAcL15HIBXigytrSz0cbZ4bQW02PzVnPNdZTVNja5K/nk+KgNH3ihROSAqCVhz92JYngdVXObVmEutNaqy2nL6SGS7xV9NZTvCSY2eJyjFSQCV5U8cgHj9wrT/AG1tLq/9M2mrGxtsZdXdzo21hggycZe0ldrJQqTqPdoiSAwHuVJoKQepL1Baq3A1fkbLAZy9xmkYPNZWttY3EsK38DHq0s4+JfyKOejjhFPXjnuzQZSlB6em9Q5/TV899pzOZPDXckRheewu3t5GQkEoWQgleVU8fbkD+FTns16sNe6JhlsdTibWuO8XFut7eeO5gfuWLfUFHaRT2IKv2I4TqVAINeaUGnO3W5m0++mlcZb5ODT9zkZZSzaczHhnnhuI0JYxxyD9ooQsRIq/lJ56kMq8lul6RNA6uymRzOEyN7pe/u/F4oLO2g/D7foqKetuqIfkqkniQfJi3v8AY551OejfVbvLp3xx3GastQW0VsLeODLWavxx14kMkfSV34Xjl3bnsSeTwQHQblejzcXA31omjJodY2k0RM0oMVjJbuD+UpLLwykEEMrE8hgQvALQ/wDyT7p/5NNZ/wCgrn/Uq023HrVxX4HN/KNgL38W+pbw/gFmv0/g6r17ea47d+3fnj246/v5rpv56u1n+INZ/wCZ23+0UFbdpfTPuXrXM26ZfBZPS2FaWSK5yN/ahJISsZdSLeR45HVm6r2Uccsff4kVYXbH0aab03q+1zeqNTfrVZWv7SPGvjBbxSSgjqZf2r90HuenADHjkleVb97/ANbG2yWNw9jprVs92sTGCKaC3ijd+PirOJmKqTwCwViB78H7VCWb9ZO7mQxc1naW2mcRNJ163lnYyNLHwwJ6iaR09wCDyp9ieODwQFs9zt19stlNIXVjaPhUvcf+ztdM4p4opfLIDIoMSf3lD2Ls5Xjg8gMzKrUZ34351luplLmKW9vcRpqTp4sHFchol4WPnyMqIZv2kfcdwehPx4/fHOqs/mdU6ivdQ6hyM2Ryl9L5bi4lPyc/YAAeyqAAAoACgAAAACvMoFKUoFKUoFfbgsXf5zOWGExcH1F/kLmO1tYu6r5JZGCovLEAcsQOSQP418VTb6KdD2utt9ceby+mtYtPxDOKsSgtO8E0QSMk/lXu6kngkhSBwT2AXS9YOUv8P6bdY3eOn8E0ltFas3RW5innjhlXhgR8o5HXn7jnkcEA1mBV7P0hO5keI0lb7YWcEM13nYku795O/a3t45laLp7BSzyRMOeT1EbAr81YVg9L+ls7qje/TH4FY/V/hGStMpfftUTxWsVzF5JPmR247D4ryx59gaC8vo00Lf6D2NsLTMWV7YZbKXMuSvbW6K9oWfhI16gcpzFHExVuWDMwPB+Ion6l8/mdQ766wlzWRmvWscvdY+0Eh+MFvDM6RxoB7KoA/d9yWY8sxJvz6utV3+j9gdQ5TD5r8Iy0vgtbKZJFSVmkmQSLET79/F5TyvyUKWHBXkZp6Twl1qXVWJ05YyQx3eVvobKB5iRGryuEUsQCQvLDngE8fuNBcb9Hbtrf4+zyO6ORPihyds2PxUaTKfJEJv28jqByP2kKKvyB+MnK8FCY/wD0hGurDUm5eL0vir2yvLbTltKtzJAGLR3krjyxM3PU9Vih9l/KxdSeQQtoNIvhvTl6c8Xaa2zcMy4iKQO1snyubiaWSbwQKxBduXZQT15Cl26KG65m393dX99cX19czXV3cytNPPNIXkldjyzsx92Ykkkn3JNBNnow2xv9fbp2+bjvfobDSlzaZOeXxLJ5ZVnVo4OO6le6xynuAwXp7j3FWf8AXbrTS+M2Xy+i73MQx6hzEVvNY2AVmkkSO7hZnPUEIvCPwXIDFWC8kED8fQrtbldB6HvdTZTJWVx+tttY3lrb2wY+GARM6F2YD5nzkFQCB0HDNz7VZ9Yu42C3L3fGW0zJ9RibHGwWNvd9XT6ngvKz9HRWThpmTgg89OeeDwAhmlKUClKUClKUClKUClKUClKUClKUCtTPVRgv1i9POtcf9V9L4sa1938ffn6ZluOnHI/N4uvP7u3PB44OWdaM+g7VepNWbMXtzqbNXuYubPNz2sNxeSGSUReKGQKzn5Pw0j8FiSAQPsAAGc1aWeiHN3WZ9OeBW8jyflx8txZLPeg9Z0SVihhYk9okRliH2AMTKBwtVA9ZehNUaU3ly+czks15jtQ301zi76WVWaVAI2aIL3ZlWHyJEO3UEICoA9h1n6PPVc2P3fn0veZq9isMnjbg2eP8kht5LwGJy/QfAP4YZPmePZevPuAQhnfb+m/Xn9ZMj/aZKt/+j43KsMvoR9s7keLLYPzXVqFhYLNZvKGZi/JHdZZSCOF+LR8diHI+P9IdoDO6gxeB1dgNPfWw4W2u/wAZvIFTyxQdoTF2HPd0UmZvYEIC7HqCTVefSPuZhtrd2RmtQwTNi8hYvjbieL5Nah5I3ExQAl1BjAIHvwSR2ICsHs+uTRel9Ebw2ljpTDw4m0vsQl/PBCzePzPcXAYqpJCLwigIvCgD2Aq6fpf1TgtUbIaY/Ar76v8ACMbaYu+/ZOniuoraLyR/MDtx2HyXlTz7E1xnrd2wxWsNqMlq23xfk1Lp62+ot7mJ1jZrVXDTxyFvZ0WMySAfmDL8fzMrV59BO5mG0Vr2/wBLZqCZV1ZLaW1pdx/JYrhGkWON1A56yGbjsPykLyOpLKEJbqaOv9v9w81o7Iv5ZsZcmNZeFHmiIDRS8KzBe8bI3Xkle3B9wa5mr2evraK61Hhl3RxFzNLd4OxW2v7ARlw9qJGbyx9QSGQysz9vj0BblehD0ToFKUoFKUoFKUoFKUoFKUoFKUoFKUoFX/8A0f23mKwm2A3B8v1OW1H5I+XhUfSQQzyR+NG92Pdk7seQDxGOvKcmsHpl2Wz+6eqre+GPhOlcbfQHLT3UrxRzoHQyW8TIOzSmMk+3AUEcsvZebs+qHX8mz+yTXmmLWGzvpZYcTh1itkMFmSrEHpyFCpFG/UcMAwQFSvNBTP1ra4tdbb65AWdjNaxafiODZpWBad4JpS8gA/Kvd2AHJJCgngnqJ/8AQHtPmdK2OT19qTGw20uasbdMMwuu8htJAJncqhKhX/YcdvmDG3IUH5VN2H2/utzd0cRpSFZltJpfNkZ4gQYLVPeV+wVgrEfBSw693QH71olu5r7Tew21mOu/wa9ubC28WJxdlbSA8MsDmJHkkbkJ1h6l/mw9jw1BTP1168xWtN37a30/mPxPE4fGx26yQXKzWjzuWlkkhKMVPKtEjH2PaLg+yg1036PPbz8a13e7h3ct7BDp39hZKsPEVzPPFIkgMh9j442BKD35ljJIA4atmlcBmdU6istPaex02Ryl9L4re3iHyc/ckk+yqACSxICgEkgAmtRdG4nFbP7IR/UYyyh/AcILvMfhMCr9XPBbL55RyE7u/j/M/BPtyR+4IA/SL6603PpvFbd2179Rn4MlFkrqKIBltYhDKqrIefZ28oYL7nqOTwCnas3p10dYa+3q0zpXKP1sLu5aS6Xhv2sUMbzPFyrKV7rGU7A8r25HPHFeZvBri63H3JzOtLyxhsJclKhW2iYssSJGsaKWP5m6IvLcAE8kBQeBeX0K7b5nQW3WVvNT4CbEZrM3yS9ZpeZHtFhQwhkDHxsHkn5Vgrgnhh7DgOt3319YbD7MWlzhMN9R4PDhsNavIzRRMIm8ZlYt3KKkR+xLMQByOS4zAqxnrs3Kv9T7n3eh1GFmw+m7kC2ubaFXuGleCPzI8pJI6yd1KJ1HKjuGZFK1zoFKUoFKUoFKUoFKUoFKUoFKUoFKUoFTb6KtaXWlN+MJYvmJrLD5yU2F9AFLx3Lsji2BUA8N5mQBxwVDNyQrNzCVKDRn156WzuqNkI/wKx+r/CMkMpfftUTxWsVtceST5kduOw+K8sefYGqAaJ1TndF6ntNTaZvvoMtZ9/p7jxJJ07oyN8XBU8qzD3B+/wDGtGPS5rjRu4mzGM0zZH62bC4S0xmbx95aHqv7JoeG7ApIkgicgAn4kdgpPFUa9Su1v8ke5cmm4cl+IWFzbLfWErjiVYHd0CS8ADurRsOV9mHDcLyVUNEocpgN49nskmnMzCLTP4iWzeVGSeSxee390lRHIEqCVS0fYHn259+azA3F0hmdBa1yekdQJCuRx0oSUwyd43DKHR1P/FZGVhyAQDwQDyBPP6PzcPFaV3DyOkcpF4/1q8EdreNMqJFPCJSkbBuOfJ5CqkHnv0UKe3Kyb669kr/Un024ujsVe5DMJ47PJ2FjarI88XyCXAC/N3UlYz7OSnQ/FYySEmekDc+53M2oS5zeU+u1LjbmS3yrMkMTN2dnhkEcfACGMhASq8tHJ9+CTU31daWzu2vqGn1ribH8KssjklymFu/Kk3kuo1hlnk6MWI4ncnq4CnngDr7VHOxW4t1tZuTY6vt7Sa/igimhuLGO7Nut0jxsoR2Ctyofo/BUjlF+xAI0l1DgNI717TWcWax00mHzljBkLQyBUubQyRh45EI7BJVD/u5B5ZT2UkEOM9NW8mG3r0VdYrUEeM/WOKKVMviRBxBPbuxUPGjs/kiKMqPyTwxIIAZO1QPVTsbkdp9RHK2Zhn0rlr6YY0wrKWsx7OsExYEBuGZUPdi4iZjx7geLoTUet/TnvLI99ioY8paRLbZXGSyxyLNbyiOXxiRCwViPGwZSeCByCOynQy3u9F727TXMNvcw3+FzliIbhI5IZZrN3jVwjgd1juIuyNweSjBT+4UGUFKk3f7ZvUm0up5bK8hvchg28Qs839GYre4Z0LFPZnCOGWQdC3YhO3HBFRlQKUpQKUpQKUpQKUpQKUpQK6ba3RWV3E13jtHYS4sre/yHl8Ul47LEvjieU9iqsfyoeOAffj/pr49G6U1JrLOR4TS2FvcvfycHxW0ZbopZV7ufsiBmUF2IUcjkitGPTtsxpvZHSFzlMpd2U2fltjJmMxKwSKCJR3aKNm46QrxyWPBcr2bgBVQOm240dpPZPaya0t3+nsMfbNkMxe8St55Y4FE9x4yzleyxdvGnIH2A/jnPv9udf7tbhy6qvLL8PhW2itbOy8qy/TxICSvkCIX5kaR+SOR34+wFSZ6wt/b/AF9nLzROm7j6fSOPuWjlkhlVvxWWNv76WUkGEMOY1BIPs7e/UJIHoR2Sv4Lj+U7V+Ksvori2Awdpe2qySlvJHIt6vb+9cdOI2A7MGLDqvUuE2+mTbi62V2mvsZqnN4ySVr6fKXlxE5S2tU8aJ7ySdeVCQhyxCgdiPsvY0z9ZO5Emvd3L6zx+fhy+mMNL4sQ0MSCNC0UIuCrhQ0imWM8MSwIHKnqRzYX12byWGC0xd7X4ebz5jL2wGRltrxo3x0XeNgjgKQ3mj8ilOykIQSCrjmsHpr2nzO6OvbNIMbDdaext9bPnnluvEqW7MzFBwRIWdYpFHQexI5Kj5ALAfo8Ns41sbzdS+nycNw8suNx9uO8MEsICGSYkEedS/KAH4q0TH3YKU+L9IfuRHPNjducHn5g1tK8uocfHE6KSUgktQ7lQHXh3bqrEchSw7KvFjN9dcWu0GzV9nsVY4xZbGKGzxOPkYQQs7FUREReOVROz+NeCVjYAqPkMx89kMrrTXF/lPovNls9kpLj6WyiZu888pbxxpyWPLNwo5J+w9zQdz6Z9po93tenBz52HGWlnELu9QK5uZbcMFbw/AxhuzRqS7DjyBgr9StX59S248O2u1GYy1tkLKHPy2zR4i3luI0lklZ0jMsaOD5PF5RIV6kELweAea8z0jbdR7e7NYpLzEw2WocrEL3LP0cTMWLNFHJ3AZWjjZVKcAK3fjksWanPq43rsN3c5jrTF4j6WwwFzex2t79Sz/XxSNGEl8bRoYuViDdTyfnwft7hD+qs/mdU6ivdQ6hyM2Ryl9L5bi4lPyc/YAAeyqAAAoACgAAAACvMpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgUpSgmb0i7lak0LunjcJhxZS2GqMlY4/IxXMJb4mcKJEIIKuqySAe5X5HlTwOLs+qvbD+U/ai+x+Nxdld6lseLjDSzv42Rw6mWNX+w8kasvDfAt0LcdQy5gVfL0E7r6byGhLHay5f6DP4vzyWqyuOuQieV5mMZ9uHTueU9z1XsCR3CBSf8A3d0Nrj/F+f0/kv8A4Jfp7q3l/wDqRurp/wA6nj94rR/0pbsR7o7bW75HJQ3WqsbEqZtIrV4lQtJKsLnkBCzpF2PQ8Ak+y+yivPrf2L/BsodwdFYbNXsOTubu71AIz54rN+qyeUKB3RGIndmYlFPA5QFQYG2O3MzO0+vYNU4eCG6UxG2vbSX2W5t2ZWaMNwSjcopDD7FRyGXlSHWerjai/wBs9y7m7VLL8A1Bc3F5ifpUWJYV7hnt/EPyePyIo4+JUqRweyrIHoj30xWivqNDa3zN7Dib25i/CJZQptMe7eQy+Rye0aOxj+wKKxZj0BZjbLW2H03vjsrd4vF5/th9QWySWuRtFD9WSRZEJVuD8ZIwHQ9W9mUlW9xmpu5oPM7ba9yWlM1DMGtpWNpcSRdFvLcsRHOgBYdWA+wY9SGU/JSAF+PVhsZYbo6Yus3h7Htrexto48dK120aTxI7MbdgeU+QkkKtwp79OXC81TPYvd7WWzOr1x0k97Dgxkl/HcLPbhm+JMcvVH6mOYLz9mXlkQPyF4qc/SX6m/8A0dt/uNc//mGh1LkMn/0yqly0x/8AnVXDf+6Tp92qTfV3sJ/Kpi49Sadk8WrsZbeGGKSXiK+gDM4gPJ4RwzMVf2BLFX9iGQO//wDNfv1t5/8AYtU6ckuf/wBSJ4Z4z/8ATLE4B/8AhJR/3q/vQDf/AGH1Vs99HeZS8sspib+5mgtby0SUdenBQTBl6xu6kkIGb8j8EheT421G5WuNmNX3tzhB9Nc/K1yWLyML+KRkJHWWPlWDo3PBBVlPYfZmU3y9O3qB03u3b3NtPFZadz8dyY4cRLkBLLcxePuJYyUTv+WTlVBKhOTwGFBmbSrzepP0o2ea+v1btpF9Llm8f/k/BDbwWkvHij/YnmNYeFEkjdu/dj7dSfeo25W2+t9uL60s9aYCbFS3kRltmMscscoB4YB42ZSw9uV55AZSQAw5DkqUpQKUpQKUr2tE6WzutNT2mmdM2P1+WvO/09v5Uj79EZ2+TkKOFVj7kfb+NB4tdbtLt/n9zda2+lNOLCt3NFJM89wHEECIpJeRkViqk9UB447Oo/fU/wCx3pAzmXvsm+7EGT09aQxRixisLy1kkuHYnsxdTIFVAoHUryxkBBHUg2s1PqbbjY3by3guprLCYmwtmXHYyBgbi56kcrChPaVyzqWYn7v2dgCWoPM2X2n0RtBpWPKjG4zHZpcRCmeyxupHjYxoGncPMf2cRcFzwEBCqSPiOKp+qb1MX+tbibS+3uTvbHScls9tfyNbLFLkGMh54YkusJRU4H7NmDyK4IIA4z1H7+ZXeS3xllLhvwOwx1zLPHbRXzTLL3jiVTIOqhnRlmIfgcLN14HBZ/T9N3py1FuTfYvPZ61msNDXUU7tkLe9hWeUoWjCRoQ7BvKPfugHVW4PJXkHpM2Gut0szFqPNJCNGY6+MF+gujHPdOI+/ijCgkLy0Xckoerno3YHrcDf7cDGbF7NWyaebGQZGCK3sNP4y9MkyzJGY1ccBg5VIeSXLAc9ASSwDezvLuZpHZXQUV5eQQqyxfTYbDWvWJrgooAjQAcRxIOvZuOEHAALFVbNrdrcDP7m61uNV6jaFbuaKOFILcuIIERQAkauzFVJ7ORzx2dj++g+LS+B1RuJrWPEYiKbM6hyssswE1yokuHCtLI7SSsAW4VmJY8k/wASa0l2I2s0vstoJ3Lw22RlsYptRZOW8YwyPErszgv1VIk8kgB6qeoBbkgmuG9F+xl/tpi7/U2r7H6XVmQ72qQrdrKttZhkPUhOULu6diQz8KIwOpLgw/65d8o9S31ztbpoTJjsZfEZi7LPGbm4iJUwBeRzEj+5LA9nRSvAQM4Rz6tt3v5Vtw/9y5++l8P3hxHa38Tydgnlmbnlj3ZB1B44RU5VWLc916D9n7XV+opdxM95jjtPX0Qx0MbhVuL1OJOzkN2CxcxN14AcuvuQrK0M7HbZ5ndjXsGlsPPDaqIjc3t3L7rbW6sqtIF5BduXUBR9yw5Kryw0e1hqLTeyOzEVxd3XeywONisMbFdTBZb6WOLrDDyqnl36DkheFHZiAqngIg9b+90mj8TBorRWpJrLVU8ofItaIjNbWjROOjOeTFKxeN16cOAvbley9qDV026WtcruJrvI6xzdvZW9/kPF5Y7NGWJfHEkQ6hmY/lQc8k+/P/RXM0ClKUClKUClKUClKUClKUClKUClKUClKUClKUCva0TqnO6L1Paam0zffQZaz7/T3HiSTp3Rkb4uCp5VmHuD9/414tKDTLYDcrTe+e1l5hMgL27v7fGw4/UkVzCIPqGmgKySIYjwEkZZgOpVh1PxX480z9WGz82124d02Hxt6ukb7xy465YSSRwM4bm2aUqB3Vo5Cq9mbx9CSTya4zZTXV/tzuXhtUWl7e29tBcxrko7UKzXNmXXzRdWIVuyg8A8cMFYEEAjSWGLb7frajH319i/xfTmT4uYorpXhlhljdlPupDI6sHQlG4I7AFlb3Cinpe35ye02ZXGZN5rrRlzLNPfWNvaxvOJmjVVljZih7cxxqQzdepb49uDVzPUZtHht8dBWMuOykMeUtImusFkY5fJbSCVVJV+vIaKQKnzXkrwrDkcq1BvUBtrf7V7l3+mbk97J+brFzGZZGms2dhGzkAcOOpVh1HyUkcqVJkz0geoCbbvKJpLV+R/8irjySJLKskjYyXqzcxhFZijt7FAOAzdwV+fcIG1VgMzpbUV7p7UOOmx2UsZfFcW8o+SH7ggj2ZSCCGBIYEEEgg1cb0s+qS5zGUh0dudd3t9mMrkkhxmTitYViHkUKsEiRKpX9oBw4DcmX5dFXmpz13orbj1A7eYy5uLj6/Gy8XOMy2PcJcQckBwjMp689ejxuvsV9wHQFc8969pdWbU5wWmobTrYXdzcx4q98kX92xQso8vjR2MfKujdW9x249+DQXs9TGwGG3YxIvMUuMwmqoZTKMkbTlrwCIoIZmQgleVi4chygQhV9yDQDU2E1ptRr2axuJMngc1YSyrb3tsZrZpU7PEZoJCFZon4cBxwGHP/OKkz05+pPP7WWNlpe+x8OW0qL5551LObuBHADLAS/jVQwMnQrwzM/yXt2F5re7263x22uYbe5h1Hpi+lENwkcksDd4pFcI4HSSNgyo3B4JBU+6sOQqzs16y8njoZbHdSwmzESRc2+QxdtGlyz9ySssZZIyvUgBk6kdByGLFhZ/R2f0DvZoSwykuEssnYT83ceNzVrBNLB1lmgWVouXC9mimCtz7gMOfuBVrfr0h52zzi5DaWy/EcTPx5Mdc5FFuLeRmkY9DIEUwqojUdnaTknnkcmqv6qwGZ0tqK909qHHTY7KWMviuLeUfJD9wQR7MpBBDAkMCCCQQaC825Xoz0Rnb60uNF5ebR8UcRS5tzDJfxzHnlXBklDI3uQfkQQF4CkEtDN/6MN2LaxuLiHKaSvJYomdLeG9mEkxA5CKXhVQx+w7Mo5PuQPeuf2x9Uu5ug9IWul7RMLmLKz+NrJlYJZJYYuB1iDJInKLweoPJAPUHqFAlPa/1qZGbUUVnuNp7GQYu4lRDf4lZUazHy5d4naQyryU56lSoDEBzwtBWz+SfdP8Ayaaz/wBBXP8AqV2eC9L+9uW+gk/U76C2vPG3nvb6CPwI/Hykj7mVeoPLL0Ljgjrz7VabN+snaPH5SaztLbU2Xhj69byzsY1ik5UE9RNIj+xJB5Ue4PHI4J5LX/rYwC6dcaB01k5M00qhWzcCJbRp92YiKYs7e3AXlR8uefj1YPj0r6H7VJrKfVOvppovFzeWmNsBGwcp+WOeRm5UPx8jFywH2Un2slhNvtstDW8OXxuktM4T8ItmIyZs4klt4ljKu73DDv8Ak7dnZuSCSxPJqmf89XdP/EGjP8zuf9oqueby2VzmUmymbyd7k7+fr5bq8naaWTqoUdnYknhQAOT9gBQXM3O9aOEn0hdW23eFzVvn5/2cV1lbeFYrVSDzKFWR+7j26qwC8nk8gdGqNr/WmqNe6ifUGrsxNlci0SwiWRVRURfsiIgCovuTwoAJZifcknptqdk9xdzbEZPSmGhnxa330U99NeRRRwPwjMWUt5CqrIrHqrHj7An2q9np/wDT3o3a63sMy1n+IauW2C3ORmmMqwSPGqyrbjqoVOwfqxXydXYFuCRQQN6QvTfdZKbB7may/DJcLLFJNbYO8x5na7R0ljDyrIAqL7xyoQJAwKn4+xqzO5Wv9vNi9FWj31rDjbFpTFj8RibaNJJiW7SGKIFVCjsWZiQOWHv2ZQ0Wb6erXSemsW1ltxc2Wps/9S0MkkkUv0VsqMOzFvj5u3uF8bFT7sW4AD0Hv7u6v764vr65muru5laaeeaQvJK7HlnZj7sxJJJPuSaDpt0dxdXbk6ilzWq8tNdMZXe3tA7C2sw3UFIYySEXhEB/e3UFizck2Z9GPp3ju4bXcjX2OxmQxd7YscViby2d25ZyvnlRwEK9F5QcOGEqv8Sq8/b6L/TysC4vdHWkM0d2ksd5grAmCSCSF4A0dzJ+c9uZAyL8GRogx55AEjeqT1GWG1fTTum4rLL6uk6SSwz9mt7GI8HmYKwJdl/KgIIB7sQOocPM9am+UmgcNPoPT4ydpqfLWMVxFkoWRI7W3eR0cq3JbynxMo4C9Q/cOGUCqJ4TF6k1zq+HG42C9zefy9yxALl5biViWd3dj/8AMzOx4ABZiACa/CwtszqzVVvZwtNks1mb5YkaabmS5uJn4BZ3P5mdvdmP3PJNaJeknY+HarTH4vmIudXZa2RciDJHKlood2EUThARypj8g7MpeMEEgA0HQbIbTaR2W0UxeTGTZGCKeXJ6imtlt5JIS3chmZm8cSoicqG68p3IBJNUt9XG9GV3L1fc6dhNlFprA5K4SwNncNIt7wRGLh2DdH5CsyFVHVZWHLckns/WX6hP1suL/bnRd5ZXWlh4lv75IezXc8chcrFIWIMIYRHsFBZkPDFCO1WaBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBUp+n7e7VG0WZ5snmyOnppWmvsMZljjuH8bIrh2RzEwJQkoAWEahuQBxFlKDVLPYTa3fvQRLSYzUOOliaO3yFqUNzYO6o56OQWglH7MsjAH2AdSOVOfW/wBs3qTaXU8tleQ3uQwbeIWeb+jMVvcM6FinszhHDLIOhbsQnbjgivi2X3e1ltLlLu80rPZNDfdPrbO8txJFcdFcR9iOHXqZGI6MvJ455HtWguFze0vqN0FNaeOHPY6KWGS7sLkPBc2M3XsvPUhkb3Ze8bFW4kUMw7Cgo16ft/8AV20199OGmz2nGiZGw1xdskcR5Zg8DEN4W7sS3CkOGPI56st+MJkNuN+NtIb02Vln8Hd9lktryIeWzn6FWVhzzDMquQGUggMGRiGDGnXqT9MGf0XNndYaPt4bvR8EomSzjuHmvLOEoDI7qUHMSP2HIZ2CdWbnh2EDaJ1TndF6ntNTaZvvoMtZ9/p7jxJJ07oyN8XBU8qzD3B+/wDGgsN6gfSXmdIWP49t3Nk9T47yqk2ONv5L+3BCgOPGB51L9ueqKUBX2YBmWv8Ab3etNvtRXMNvc6g0nmkiENwkck1lcqjdXCOB1YKfg3B9j8T/AAq7Ow/qz0jmcNiMFuJfzYvUfi8V1kpbRY7CeTydEPZGPjZkKszMqRgh/dR1FSnudsRtfuJlLrM6j07zmLm2+nORtbmSCVeFKpJwrdHdQRwXVvZVB5UAUFbNjvWJJgtOwYHcvGZPMtaRFYcvZOklzMB1CJMkhUMwHbmXvyeF5UsWc2me72h3NvorF7nQ2tLuyieaKAyWuQkgQlQ7hfkVUnoCRwOevP7qobvZ6ade7Y4a71HcT4zMaetpSJLy1m6SQoZEjiaWJ+CGcuvxjMgUg8njgmGbC7urC+t76xuZrW7tpVmgnhkKSROp5V1Ye6sCAQR7gigvxu76QNK6w1O+d0znv1S+o4+osYMXFJaL1REXwxoYvH+Vmbkt2Zufj++OdVeiPM2Onb2809rqHM5SGLvb2EuM+lW4I+6CUzMFYjnjkcE8AlQSwjPQHqj3g0lCls+dh1FaRxMiQ5uE3DKWft3MqlZmYe4HZyADxx7LxJmgPWxn11Eg19prGSYVomDNhIHS5jf7qwEsxV19uCvKn5c8/HqwRM/pl3xS+iszoObyyxPKrDIWpjAQqCC4l6q3zHCkgsAxAIVuP2/mub7f8hv+9rL/AMarM/z1drP8Qaz/AMztv9op/PV2s/xBrP8AzO2/2ig4aw9DV09jbvfblwwXbRKZ4ocKZY0fj5KrmZSyg8gMVUke/A+1TntT6ddttEaVGIvsFjNVXby+ee/zGMt5pO5RFZY+UJSLlCwQliCx+R+9V53O9aOpLrKXVtt3hbLH4l7bxxXWVtzJerKVPMoVZDEvUkdVYSA9eTyG6CH9w/UDuprzTt1p3UOoIZMPdxQJcWkVhBGshi6MHLBO4ZnjDnhgOSQAF4UBebcreTafY+xtNPGOFZUlKLg9PwQ+S0DDyl3iDIsSnuCOSCxfkAjsRT/1MeojM7kaiEGkcjqDA6VSxNq9kbnwteGTnytMsR4ZSCECMzjhSRx3YVA1Wg2f9H+rs7NhsxrqeHDYK7ieW6sorho8pCCjeMFWiaNWLdCVY8hSQQGBACvOjdKak1lnI8JpbC3uXv5OD4raMt0Usq93P2RAzKC7EKORyRV8vS36av5LM4+rdTZeyy2fa2e3t4LaDm3suzHtIkjgOzsgVeQqdQ8i/INzUgWmL2h9PekL7KQwWWlcTdXMYuJmea4luJSOEQEl5X4HYhF5CjyNwB2NVM9QHqwzus7e/wBN6HtPwXTV5bG3uZby3R726R42SVG92SNCH4HXl/gG7jsVATb6qfUna6AhOmNDXOMyuo7iKaO4uo7gSriHVwg7oFKvL7S/BmBQopdWBANDL27z+rNRLNeXOTz2av5Y4VeWR7m5uX9kRATyzt7KoHufsBTSuAzOqdRWWntPY6bI5S+l8VvbxD5OfuSSfZVABJYkBQCSQATWiXpm9PeC2uxdpmc3Z2WQ1uvnWXIxTPLFAjt1CwBlUL+zA5Yr35eQdup4oOM9FOwV/ovruJrO38Gcu7Yx47GyxL3sYn45lk5HKTMo69RwURmDclyqeN63N9sJcaQXQehNS/WXOR8cuQvcVcwzWslmRKr2xlRyyuWWMsoA5Q8E8MVL1iepCwhxeV2z0NJ9Rez+fH52+lgZVtlDNFLbxq4HZ24YGTgqqn4kse0dJqBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBXTbY661Jtzq+11Rpe9+nvYPjJG4LRXMRI7RSryOyNwPb2IIDAhgCOZpQaP7HepzQWt9OwJqnM4zS2o4oj9ZbXs3gtpCvUeSGWQ9erdgRGW7jhhwwXufM9Q3pe0rrb8f1fptb3HasntmnitbZoltL26XluXRgOry/lLh1UMQ7Ant2zzqyfp+9VmqNH334ZuFd5PVOnmiYJISst/bPyzBhI5BlVi3UrI3IHXqQF6sEGa/0XqjQWon0/q7DzYrIrEswikZXV0b7OjoSrr7EcqSAVYH3BA7nYHfbVW1Ocik8l7ncAltLb/gs+Rljt4+7B/JEPkkb9xyT0PIZx7FuwvzovKbbb66Kx+q303jMzaRyzQxQZmxt7ieycMA6MvLiNmCo/APJUoT9xUJ72+kD9aNT5fUuis9hcJ9T4fpMJ+F/T2kXVI0f9pET156u/tF7seD9y1B2eyPqn0Pr36621IbLRF/bcSRJkckht7iL2HKzMqDuGPuhHPHBUt8usjZuLbbePSuU04mX0/qa0ERWV7G5t7uSxeRHRJkPzEUoBfo5HPIPH76zA1ronV2ir4WerNOZPDStLJFE11bskcxjIDmJ/yyKOR8kJHDAg8EV5mEy2VweUhymEyd7jL+Dt4rqznaGWPspU9XUgjlSQeD9iRQXf1J6I9Fz2KJpzWWoMddiUF5b+OG7jKcHlQiLEQ3PU9uxHAI49+RCesvSPu9h85JaYLG2WpbD3aG9tr2GDlezBQ8czqVfqAxC9lHYAM3Br4tG+q3eXTvjjuM1ZagtorYW8cGWs1fjjrxIZI+krvwvHLu3PYk8ngibMP64MBLNaDMaBydpE0soumtb9LhokCKY2QMsfdmfsGUlAoAILklQFec36bt7cPi5sjd6BvZYYevZbO5gupTywUdYoZGdvcjnhTwOSeACa/HTfp43pz9i95Y7f5OGJJTEVv3ispOQAeQk7IxX3HyA455HPIPFrP56u1n+INZ/5nbf7RT+ertZ/iDWf+Z23+0UFedN+knenK3z299h8ZgYliLi4v8lE8bHkDoBAZG7Hkn3UDhT788Azbo30S6Vjwcf646szV1lm4aT8JMUFvFyq8oPJG7Pw3b5/DkEfBSDz+GY9cGAimuxh9A5O7iWWIWrXV+lu0qFGMjOFWToyv1CqC4YEklCAphPN+rDe3IZSa8tNR2WIhk69bOzxkDRR8KAepmR39yCTyx9yeOBwAF5dO3G2WzumMToN9WYXBw2Nt2t4ctloo7iVXdy0pDsCe0nkPIAXnkAADgQzv96t7DSGcl0/t9Z4XU0y20Uhy31rS2kUrMS0XSMAS/s+vyWUAM/B90Zao1m8tlc5lJspm8ne5O/n6+W6vJ2mlk6qFHZ2JJ4UADk/YAV6e32js/rvVVnpzTlhNdXdzKiu6Qu8dsjOqGaUorFIlLr2fjgA0Htbi7t7h69vsnLqDVOTaxyMoeXFw3UiWCBSCiLB269V6rxzySR2JLck+nsXsprLdrKL+DWv0mDhuVgv8vOB4rflSxCqSDK/Xj4L9iydigYNVrPTz6UrXROWkzevrrT+p5Z7GS2bFSYwXFtA5lRllSSX8zdE4/vakd2HJA5Mp7pbi6B2G0hi/q8V9JYXFy1vZYvC28CMOQ0kkixFkHQMR2I+zSLz+ag+La3abbLYfF5TN2199P5+q3WZzl3ErRRFlCxCTqiIhfg8cAsxXknhAK5+qv1PZXJZS+0VttkvocZaXIWbP468by3vVVJWJwFMaCTuCylvIFUhghIaMvUJ6gNWbnZTLYu0yN7YaKnuY5LXEusSsVjUBTK6KGbswMnQsyqxHBPRWqGaBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKBSlKD97C7urC+t76xuZrW7tpVmgnhkKSROp5V1Ye6sCAQR7girZbOesDV17rXTuC13Bp9cLPKlpfZKO3aGcFl6LM7NKIkXuVZyFAC9+APYVUalBqlorfPaXWN8bHA65xkl2ZY4Y4LrvaSTPISESJZ1QysSOOE5IJHP3HPP659Me0OrLjK39zg72wy2UuXurjI2eRm8oleTyOyrIzxDsSQR0IAY8cHgjM2pAwm9e7mHykORtNx9TSzQ9uq3mQkuojypU9opiyN7E8cqeDwRwQDQTnrb0Vaq/We7/UrP4X8A+H0n4veS/V/kXv38Vv0/P344/weOffmoy/mub7f8hv+9rL/wAapG0B61NUYjTqWOrtLw6nyKSsRkI7xbJnQ+4V40hZSw9x2XqCOvI5BZu60x63tK3H1H6zaHzWN69fp/w66ivPJ9+3bv4enHx447c8n7ce4Vy/m3b2/jn4P+oN79T9N9T3+pg+n6duvHn8ni78/wDs+3fj34496Zv03b24fFzZG70Deyww9ey2dzBdSnlgo6xQyM7e5HPCngck8AE1cDRvq52j1FnI8XcSZrT/AJeFjustbRpblyyqFLxyP0/Nz2cKgCklh7c+zub6l9rNDfh/+636zfW+X/1euLa8+n6dP77+1Xr27/H789W/hQUzwnpf3tylvDcjR30UM1s1xG15fQRN/ey6xtH37o7EBAGUdWYd+oBI6DRXpA3azV8Uz0GM0xaRyxiSW6vEuJHRie7RJAXDMoHPV2QEkAH7kTNqT1uaLgsUfTmjdQZG7MoDxX8kNpGE4PLB0aUlueo69QOCTz7cHmb/ANct09jcJY7aQwXbRMIJZs0ZY0fj4syCFSyg8EqGUke3I+9BI2E9G20ePykN5d3OpsvDH27Wd5fRrFJypA7GGNH9iQRww9wOeRyDI2v98dq9B6ifT2qdWw2WUjiWWS3jtZ7how3uocxIwViOD1JB4KnjhgTnbm9693MxlJsjd7j6mimm69ls8hJaxDhQo6xQlUX2A54UcnknkkmuGv7u6v764vr65muru5laaeeaQvJK7HlnZj7sxJJJPuSaC0u8frA1Le5nUWC0JBjF05PE9pY5KS3nhvwGj6NMjLKOjdyzISoIHTkA8iqp0pQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQKUpQf/9k=" alt="Humaniza" width="44" height="60" ></th>
        <th bgcolor="black" ALIGN=LEFT style="width:20%"><font color="white" face="monospace" size="2"><br/>Hospital</font><br/><font face="sans-serif" color="white" size="5"><b>Humaniza</b><br/></font>.</th>
        <th bgcolor="black" ALIGN=CENTER><font color="white" face="monospace" size="5"><br/>SOLICITAÇÃO DE<br/>PROCEDIMENTO HOSPITALAR<br/></font>.</th>
        <th bgcolor="white" style="width:20%"></th>
      </tr>
    </table>
    <br/>
    ''' + f'''
    <table class="table2" style="width:100%">
        <tr>
            <td><b>Identificação:</b></td>
        </tr>
    </table>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:2%">Nome:</td>
            <td style="width:98%"> <span class="statistics_lines">{field_nome}</span></td>
        </tr>
    </table>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:2%">Código:</td><td style="width:25%"><span class="statistics_lines"> </span></td>
            <td style="width:2%"><font color="white">_</font>Idade:<font color="white">_</font></td><td style="width:12%"><span class="statistics_lines">{field_idade} anos</span><font color="white">_</font></td>
            <td style="width:18%">Data de Nascimento: ____/____/____</td>
        </tr>
    </table>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:2%">Sexo: ____________________<font color="white">______________________________________</font>Telefone:__________________________</td>
        </tr>
    </table>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:2%">Endereço:</td>
            <td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td>
        </tr>
    </table>

    <br/>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:23%"><b>Justificativa de atendimento:</b></td><td><span class="statistics_lines">{first_line_justificativa}</span></td>
        </tr>
    </table>
    <table class="table2" style="width:100%">
        <tr>
            <td><span class="statistics_lines">{second_line_justificativa}</span></td>
        </tr>
        <tr>
            <td><span class="statistics_lines">{third_line_justificativa}</span></td>
        </tr>
        <tr>
            <td><span class="statistics_lines">{forth_line_justificativa}</span></td>
        </tr>
    </table>

    <br/>
    <table class="table3" style="width:100%">
        <tr>
            <td style="width:30%"><b>Tempo de Existência da Doença:</b></td>
            <td style="width:4%">{anos}</td>
            <td style="width:8%">Anos</td>
            <td style="width:4%">{meses}</td>
            <td style="width:8%">Meses</td>
            <td style="width:4%">{dias}</td>
            <td>Dias</td>
        </tr>
    </table>
    <br/>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:14%">Exames Anteriores:</td><td><span class="statistics_lines">{field_exames}</span></td>
        </tr>
    </table>
    <table class="table22" style="width:100%">
        <tr>
            <td>Hipótese Diagnóstico:</td>  
            <td><span class="statistics_lines">{field_hipotese}</span></td>  
            <td><font color="white">_</font>CID 10:</td>  
            <td><span class="statistics_lines">{field_cid}</span></td>
        </tr>
    </table>

    <table class="table2" style="width:100%">
        <tr>
            <td>Tratamento Proposto: ________________________<u>NO VERSO</u>__________________________<font color="white">___</font>Cód. AMB: _____<u>NO VERSO</u>____</td>
        </tr>
    </table>
    <br/>
    <table class="table4" style="width:100%">
        <tr>
            <td style="width:10%"><b>Acidente:</b></td>
            <td style="width:3%"></td>
            <td style="width:8%">Sim</td>
            <td style="width:3%"></td>
            <td style="width:20%">Não</td>
            <td style="width:15%"><b>Procedimento:</b></td>
            <td style="width:3%">{field_ambulatorio}</td>
            <td style="width:14%">Ambulatório</td>
            <td style="width:3%">{field_internacao}</td>
            <td>Internação</td>
        </tr>
    </table>
    <br/>
    <table class="table42" style="width:100%">
        <tr>
            <td style="width:10%"><font color="white">____</font></td>
            <td style="width:3%"></td>
            <td style="width:8%">Trânsito</td>
            <td style="width:3%"></td>
            <td style="width:20%">Trabalho</td>
            <td>N° de dias solicitados:</td>
            <td><span class="statistics_lines">{field_duracao} dias</span></td>

        </tr>
    </table>
    <br/>
    <table class="table5" style="width:100%">
        <tr>
            <td style="width:44%"><font color="white">____</font></td>
            <td style="width:15%"><b>Anestesia:</b></td>
            <td style="width:3%">{field_local}</td>
            <td style="width:14%">Local</td>
            <td style="width:3%">{field_geral}</td>
            <td>Geral</td>
        </tr>
    </table>
    <br/>
    <table class="table5" style="width:100%">
        <tr>
            <td style="width:44%"><font color="white">____</font></td>
            <td style="width:15%"><font color="white">____</font></td>
            <td style="width:3%">{field_urgencia}</td>
            <td style="width:14%">Urgência</td>
            <td style="width:3%">{field_eletiva}</td>
            <td>Eletiva</td>
        </tr>
    </table>
    <br/>
    <br/>
    <table class="table7" style="width:100%">
        <tr>
            <td style="width:50%" align="center">____________________________________________________</td>
            <td align="center">{dia}/{mes}/{ano}</td>
        </tr>
        <tr>
            <td style="width:50%" align="center">Assinatura com carimbo do médico solicitante</td>
            <td align="center">Data da solicitação</td>
        </tr>
    </table>
    <br/>
    <!hr size="2" width="100%">
    <hr>

    <table class="table22" style="width:100%">
        <tr>
            <td>Tratamento autorizad:</td>  
            <td><span class="statistics_lines"><font color="white">º</font></span></td>  
            <td><font color="white">_</font>Cód AMB:</td>  
            <td><span class="statistics_lines"><font color="white">º</font></span></td>
        </tr>
    </table>

    <table class="table2" style="width:100%">
        <tr>
            <td><td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td></td>
        </tr>
        <tr>
            <td><td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td></td>
        </tr>
    </table>
    <br/>
    <table class="table5" style="width:100%">
        <tr>
            <td style="width:0%"></td>
            <td style="width:20%">Regime de atendimento:</td>
            <td style="width:3%"></td>
            <td style="width:14%">Ambulatório</td>
            <td style="width:3%"></td>
            <td>Internação</td>
        </tr>
    </table>
    <br/>
    <table class="table7" style="width:100%">
        <tr>
            <td>Nº de dias autorizados:  __________________________________________________</td>
        </tr>
    </table>
    <br/>
    <br/>
    <table class="table7" style="width:100%">
        <tr>
            <td style="width:50%" align="center">_____________________________________________</td>
            <td align="center">_____________________________________________</td>
        </tr>
        <tr>
            <td style="width:50%" align="center">Assinatura Autorização Técnica</td>
            <td align="center">Assinatura Autorização Administrativa</td>
        </tr>
    </table>
    <br/>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:2%">Observações:</td>
            <td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td>
        </tr>
    </table>
    <table class="table2" style="width:100%">
        <tr>
            <td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td>
        </tr>
        <tr>
            <td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td>
        </tr>
        <tr>
            <td style="width:98%"> <span class="statistics_lines"><font color="white">º</font></span></td>
        </tr>
    </table>
    <p class="break">VERSO</p>
    <br/>
    <h2> JUSTIFICATIVA E CÓDIGOS </h2>
    <br/>
    <div>
        <label>Nome do Paciente:</label>
        <span>{nome.upper()}</span>
    </div>
    <br/>
    <div>
        <label> Justificativa:</label>
    </div>
    <div>
        <a>{justificativa}</a>
    </div>
    <br/>
    <br/>
    <br/>
    <div>
        <h2> CÓDIGOS SOLICITADOS </h2>
        <br/>
        <br/>
        <table class="table100" style="width:100%">
            <tr>
                <th style="width:30%">Código CBHPM</th>  
                <th style="width:60%">Descrição do Código</th>  
                <th style="width:10%">Quantidade</th>           
            </tr>
            <tr>
                <td>{code1}</td>
                <td>{cx1}</td>
                <td>{qx1}</td>
            </tr>
            <tr>
                <td>{code2}</td>
                <td>{cx2}</td>
                <td>{qx2}</td>
            </tr>
            <tr>
                <td>{code3}</td>
                <td>{cx3}</td>
                <td>{qx3}</td>
            </tr>
            <tr>
                <td>{code4}</td>
                <td>{cx4}</td>
                <td>{qx4}</td>
            </tr>
            <tr>
                <td>{code5}</td>
                <td>{cx5}</td>
                <td>{qx5}</td>
            </tr>
            <tr>
                <td>{code6}</td>
                <td>{cx6}</td>
                <td>{qx6}</td>
            </tr>
            <tr>
                <td>{code7}</td>
                <td>{cx7}</td>
                <td>{qx7}</td>
            </tr>
            <tr>
                <td>{code8}</td>
                <td>{cx8}</td>
                <td>{qx8}</td>
            </tr>
        </table>
    </div>
    <br/>
    <br/>
    <div>
        <h2> ÓRTESES, PRÓTESES E MATERIAIS ESPECIAIS (OPME) </h2>
        <br/>
        <br/>
        <table class="table22" style="width:100%">
                <tr>
                    <th style="width:34%">OPME</th>  
                    <th style="width:60%">Fornecedores</th>  
                    <th style="width:6%">Quantidade</th>           
                </tr>
                <tr>
                    <td>{opme1}</td>
                    <td>{forn1}</td>
                    <td>{qo1}</td>
                </tr>
                <tr>
                    <td>{opme2}</td>
                    <td>{forn2}</td>
                    <td>{qo2}</td>
                </tr>
                <tr>
                    <td>{opme3}</td>
                    <td>{forn3}</td>
                    <td>{qo3}</td>
                </tr>
                <tr>
                    <td>{opme4}</td>
                    <td>{forn4}</td>
                    <td>{qo4}</td>
                </tr>
                <tr>
                    <td>{opme5}</td>
                    <td>{forn5}</td>
                    <td>{qo5}</td>
                </tr>
                <tr>
                    <td>{opme6}</td>
                    <td>{forn6}</td>
                    <td>{qo6}</td>
                </tr>
            </table>
        </div>

    </div>
    <br/>
    <br/>
    <br/>
    <br/>
    <br/>
    <p><font color="white">___</font> _____________________________________________________<font color="white">_________________</font>{dia}/{mes}/{ano}  </p>
    <p><font color="white">__________________</font> Assinatura e Carimbo</p>

    </body>
    </html>
    '''
    return html_string
