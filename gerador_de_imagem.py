from PIL import Image, ImageDraw

largura, altura = 400, 400
imagem = Image.new('RGB', (largura, altura), 'white')
desenho = ImageDraw.Draw(imagem)

x_centro, y_centro = largura//2, altura//2
raio = 100
cor = (255, 0, 0)
desenho.ellipse((x_centro - raio, y_centro - raio,
                x_centro + raio, y_centro + raio), fill=cor)

imagem.save('imagem_gerada.png')

imagem.show()
