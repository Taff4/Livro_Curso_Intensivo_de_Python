import pandas as pd

file_name = 'Dashboard_Pro_TI.xlsx'
writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
workbook = writer.book
worksheet = workbook.add_worksheet('Dashboard')

# --- CONFIGURAÇÕES DE CORES E ESTILOS ---
color_bg      = '#0F0F0F' # Fundo ultra dark
color_card    = '#1E1E1E' # Cor dos blocos (cards)
color_text    = '#E0E0E0' # Texto claro
color_accent  = '#00FF41' # Verde "Matrix" para detalhes
color_border  = '#333333' # Bordas sutis

# Estilos de Formatação
style_base = workbook.add_format({'bg_color': color_bg, 'font_color': color_text, 'font_name': 'Segoe UI', 'font_size': 10})
style_title = workbook.add_format({'bg_color': color_card, 'font_color': color_accent, 'font_name': 'Segoe UI', 'font_size': 16, 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1, 'border_color': color_border})
style_header = workbook.add_format({'bg_color': '#2D2D2D', 'font_color': '#FFFFFF', 'bold': True, 'align': 'center', 'border': 1, 'border_color': color_border})
style_cell = workbook.add_format({'bg_color': color_card, 'font_color': color_text, 'border': 1, 'border_color': color_border})

# Formatos de Categoria (Cores do seu Prompt)
fmt_aws     = workbook.add_format({'bg_color': '#1A237E', 'font_color': '#FFFFFF', 'border': 1, 'border_color': color_border, 'align': 'center'})
fmt_python  = workbook.add_format({'bg_color': '#1B5E20', 'font_color': '#FFFFFF', 'border': 1, 'border_color': color_border, 'align': 'center'})
fmt_english = workbook.add_format({'bg_color': '#F9A825', 'font_color': '#000000', 'border': 1, 'border_color': color_border, 'align': 'center'})
fmt_work    = workbook.add_format({'bg_color': '#424242', 'font_color': '#FFFFFF', 'border': 1, 'border_color': color_border, 'align': 'center'})

# --- PREPARAÇÃO DA PLANILHA ---
worksheet.hide_gridlines(2) # Remove as linhas de grade para parecer um app
worksheet.set_column('A:Z', 2, style_base) # Colunas de espaçamento finas
worksheet.set_column('B:I', 15) # Largura do cronograma
worksheet.set_column('K:O', 18) # Largura das métricas

# Título Principal
worksheet.merge_range('B2:O3', 'SISTEMA DE GESTÃO ESTRATÉGICA - TI & LOGÍSTICA', style_title)

# --- 1. CRONOGRAMA SEMANAL (Posição: Coluna B) ---
worksheet.write('B5', '📅 CRONOGRAMA', style_header)
dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
for col, dia in enumerate(dias):
    worksheet.write(4, col + 2, dia, style_header)

horarios = [f"{h:02d}:00" for h in range(8, 24)] + ["00:00", "01:00", "02:00"]
for row, hora in enumerate(horarios):
    worksheet.write(row + 5, 1, hora, style_header)
    for col in range(2, 9):
        # Lógica de preenchimento (resumida para o visual)
        if hora in ["09:00", "10:00", "11:00"] and col <= 6:
            worksheet.write(row + 5, col, 'AWS Cloud', fmt_aws)
        elif hora in ["13:00", "14:00", "15:00"] and col <= 6:
            worksheet.write(row + 5, col, 'Python/Dev', fmt_python)
        elif hora in ["08:00", "16:00"] and col <= 6:
            worksheet.write(row + 5, col, 'English', fmt_english)
        elif (hora >= "17:00" or hora in ["00:00", "01:00"]) and col <= 6:
            worksheet.write(row + 5, col, 'Logística', fmt_work)
        else:
            worksheet.write(row + 5, col, '', style_cell)

# --- 2. CALCULADORA DE GANHOS (Posição: Coluna K) ---
col_start = 10
worksheet.write(4, col_start, '💰 FINANCEIRO (SEMANAL)', style_header)
worksheet.merge_range(4, col_start, 4, col_start + 4, '💰 FINANCEIRO (SEMANAL)', style_header)

headers_fin = ['Dia', 'Horas', 'Valor/h', 'Subtotal', 'Status']
for i, h in enumerate(headers_fin):
    worksheet.write(5, col_start + i, h, style_header)

for i, dia in enumerate(dias):
    r = 6 + i
    worksheet.write(r, col_start, dia, style_cell)
    worksheet.write(r, col_start + 1, 7 if i < 5 else 0, style_cell)
    worksheet.write(r, col_start + 2, 20, style_cell)
    worksheet.write_formula(r, col_start + 3, f'=L{r+1}*M{r+1}', style_cell)
    worksheet.write(r, col_start + 4, '✔ Recebido' if i < 3 else '⏳ Pendente', style_cell)

# --- 3. TRACKER DE HÁBITOS ---
worksheet.merge_range(16, col_start, 16, col_start + 4, '🚀 TRACKER DE PERFORMANCE', style_header)
habitos = ['Labs AWS', 'Desafios Python', 'Inglês 1h']
for i, hab in enumerate(habitos):
    r = 17 + i
    worksheet.write(r, col_start, hab, style_cell)
    for c in range(1, 5): worksheet.write(r, col_start + c, '●', style_cell) # Indicador visual

# --- 4. BACKLOG ---
worksheet.merge_range(22, col_start, 22, col_start + 4, '📚 BACKLOG DE ESTUDOS', style_header)
backlog = ['Python Mundos 2, 3 e 4', 'Certificações AWS', 'Projetos de Portfólio']
for i, item in enumerate(backlog):
    worksheet.write(23 + i, col_start, '☐ ' + item, style_cell)
    worksheet.merge_range(23 + i, col_start, 23 + i, col_start + 4, '☐ ' + item, style_cell)

writer.close()
print("Dashboard Profissional gerado com sucesso!")