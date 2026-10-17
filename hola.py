from customtkinter import *
from colores_estilos import *

ventana = CTk()
ventana.title("hola")
ventana.geometry("720x800")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)

quetzal_0 = CTkFrame(
    master = ventana,
    corner_radius= 0,
    fg_color= COLOR_FONDO
)

quetzal_0.grid(
    row = 0,
    column = 0,
    sticky = "NSWE"
)

#columnas
quetzal_0.grid_columnconfigure(0, weight=1)

#filas
quetzal_0.grid_rowconfigure(0, weight=1)
quetzal_0.grid_rowconfigure(1, weight=1)
quetzal_0.grid_rowconfigure(2, weight=1)
quetzal_0.grid_rowconfigure(3, weight=1)
quetzal_0.grid_rowconfigure(4, weight=11)

quetzal_converter = CTkLabel(
    master = quetzal_0,
    text="QUETZAL CONVERTER",
    **ESTILO_LABEL_TITULO,
)
quetzal_converter.grid(
    row = 0,
    column=0,
    sticky = "EWN",
)
#mensaje
mensaje1 = CTkLabel(
    master = quetzal_0,
    text = "Convierte tus quetzales a monedas internacionales",
    **ESTILO_LABEL_NORMAL_TRANSPARENTE,
)
mensaje1.grid(
    row = 0,
    column = 0,
    sticky = "EWS"
)

quetzal_1 = CTkFrame(
    master =quetzal_0,
    corner_radius=200,
    fg_color= COLOR_AZUl,
)
quetzal_1.grid(
    row = 2,
    column = 0,
    sticky = "EWN",
    padx = 60,
    
)

quetzal_1.grid_columnconfigure(0, weight=1)

#filas
quetzal_1.grid_rowconfigure(0, weight=1)
quetzal_1.grid_rowconfigure(1, weight=11)

cantidad = CTkLabel(
    master =quetzal_1,
    text = "Cantidad en quetzales (GTQ)",
    **ESTILO_LABEL_TITULO,
)
cantidad.grid(
    row = 0,
    column = 0,
    sticky ="EWN",
)

text_cantidad = CTkEntry(
    master = quetzal_1,
    **ESTILO_ENTRY,

)
text_cantidad.grid(
    row = 1,
    column = 0,
    sticky = "WNE"
)

frame_botones = CTkFrame(
    master = quetzal_0,
    corner_radius=20,
    fg_color=COLOR_AZUl,
)
frame_botones.grid(
    row = 3,
    column = 0,
    sticky = "EWN",
    padx = 60,
)

frame_botones.grid_columnconfigure(0, weight=1)

#filas
frame_botones.grid_rowconfigure(0, weight=1)
frame_botones.grid_rowconfigure(1, weight=11)

boton_calcular = CTkButton(
    master= frame_botones,
    text = "CALCULAR CONVERSIÓN",
    **ESTILO_BOTON
)
boton_calcular.grid(
    row = 0,
    column = 0,
    sticky = "EWN"
)

boton_limpiar = CTkButton(
    master= frame_botones,
    text = "LIMPIAR",
    **ESTILO_BOTON
)
boton_limpiar.grid(
    row = 1,
    column = 0,
    sticky = "EWN"
)








ventana.mainloop()