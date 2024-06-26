import tkinter as tk
from utils import style
from screens.visualizar_lista_reglas import *
import sys
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.constantes import CustomHovertip


class VisualizarInfoRegla(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.COLOR_BACKGROUND)
        self.controller = controller

        self.hecho = False
        self.canvas = tk.Canvas

    def move_to_visualizarReglas(self):
        self.controller.get_frame("VisualizarReglas")

    def movement_mouse_wheel(self, event):
        if sys.platform == 'darwin':  # for OS X # also, if platform.system() == 'Darwin':
            delta = event.delta
        else:                            # for Windows, Linux
            delta = -event.delta // 120   # event.delta is some multiple of 120

        self.canvas.yview_scroll(delta, "units")

    def init_widgets(self):
        self.regla = self.controller.reglaSeleccionada
        self.regla.generarGraficos()
        self.crearCabecera()
        frame_canvas = self.frameDatos()


        self.dibujarTablaContingencias(frame_canvas)
        self.dibujarTablaMedidas(frame_canvas)
        self.dibujarGraficoPuntos(frame_canvas)
        self.TablaDatosCubreRegla(frame_canvas)


    def dibujarTablaContingencias(self, infoReglaFrame):
        tk.Label(            
            infoReglaFrame,
            text="Contingency table",
            justify=tk.CENTER,
            **style.STYLE_TITULO_REGLAS  # Desenpaqueta STYLE,
        ).grid(
            row=0,
            column=0,
            sticky=tk.NSEW,
            padx=20,
            pady=5,
            columnspan=2
        )

        tp = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
            width=40,
        )
        tp.grid(
            row=1,
            column=0,
            sticky=tk.NSEW,
        )
        tp.insert(tk.END, "True positive (tp)")
        tp.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        tpValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        tpValor.grid(
            row=2,
            column=0,
            sticky=tk.NSEW,
        )
        tpValor.insert(tk.END, str(self.regla.tp))
        tpValor.configure(state=tk.DISABLED, **
                          style.STYLE_REGLA_BIEN, relief=tk.GROOVE,)

        tn = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        tn.grid(
            row=3,
            column=0,
            sticky=tk.NSEW,
        )
        tn.insert(tk.END, "True negative (tn)")
        tn.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        tnValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        tnValor.grid(
            row=4,
            column=0,
            sticky=tk.NSEW,
        )
        tnValor.insert(tk.END, str(self.regla.tn))
        tnValor.configure(state=tk.DISABLED, **
                          style.STYLE_TEXT, relief=tk.GROOVE,)

        fp = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
            width=40,
        )
        fp.grid(
            row=1,
            column=1,
            sticky=tk.NSEW,
        )
        fp.insert(tk.END, "False positive (fp)")
        fp.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        fpValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        fpValor.grid(
            row=2,
            column=1,
            sticky=tk.NSEW,
        )
        fpValor.insert(tk.END, str(self.regla.fp))
        fpValor.configure(state=tk.DISABLED, **
                          style.STYLE_REGLA_MAL, relief=tk.GROOVE,)

        fn = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        fn.grid(
            row=3,
            column=1,
            sticky=tk.NSEW,
        )
        fn.insert(tk.END, "False negative (fn)")
        fn.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        fnValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        fnValor.grid(
            row=4,
            column=1,
            sticky=tk.NSEW,
        )
        fnValor.insert(tk.END, str(self.regla.fn))
        fnValor.configure(state=tk.DISABLED, **
                          style.STYLE_TEXT, relief=tk.GROOVE,)
        
    def dibujarGraficoPuntos(self, infoReglaFrame):
        # Create canvas
        canvas = FigureCanvasTkAgg(self.regla.graficoPuntos, master=infoReglaFrame)
        canvas.draw()

        # Add canvas to Tkinter window
        canvas.get_tk_widget().grid(
            row=10,
            column=0,
            columnspan=2,
            sticky=tk.NSEW,
            pady=13,
        )

    def TablaDatosCubreRegla(self, infoReglaFrame):
        tituloTabla = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        tituloTabla.grid(
            row=11,
            column=0,
            sticky=tk.NSEW,
            columnspan=2
        )
        tituloTabla.insert(tk.END, "Data covered by the rule")
        tituloTabla.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)
        
        cont = 12
        contadorDatos = 0
        for dato in self.regla.datosCubre:
            entradaTabla = tk.Entry(
                infoReglaFrame,
                justify=tk.CENTER,
            )
            entradaTabla.grid(
                row=cont,
                column=0,
                sticky=tk.NSEW,
                columnspan=2
            )
            texto = "Example "+ str(self.regla.numDeDatosCubre[contadorDatos]) +": "+",".join(dato)
            entradaTabla.insert(tk.END, texto)
            color = self.regla.colorDatosCubre[contadorDatos]
            if(color == "blue"):
                entradaTabla.configure(state=tk.DISABLED, **
                          style.STYLE_REGLA_BIEN, relief=tk.GROOVE,)
            else:
                entradaTabla.configure(state=tk.DISABLED, **
                    style.STYLE_REGLA_MAL, relief=tk.GROOVE,)
                
            infoDelDato = "Example: " + str(self.regla.numDeDatosCubre[contadorDatos]) + "\n"
            for i in range(len(self.controller.dataset.atributos)):
                infoDelDato = infoDelDato + \
                    self.controller.dataset.atributos[i]+": "+dato[i]+"\n"
            infoDelDato += "Class: " + dato[len(dato)-1]
            CustomHovertip(entradaTabla, text=infoDelDato, hover_delay=75)
            contadorDatos +=1
            cont+=1

    def dibujarTablaMedidas(self, infoReglaFrame):
        tk.Label(            
            infoReglaFrame,
            text="Table of measures (%)",
            justify=tk.CENTER,
            **style.STYLE_TITULO_REGLAS  # Desenpaqueta STYLE,
        ).grid(
            row=5,
            column=0,
            sticky=tk.NSEW,
            padx=20,
            pady=5,
            columnspan=2
        )

        confianza = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
            width=40,
        )
        confianza.grid(
            row=6,
            column=0,
            sticky=tk.NSEW,
        )
        confianza.insert(tk.END, "Conf")
        confianza.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        confianzaValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        confianzaValor.grid(
            row=7,
            column=0,
            sticky=tk.NSEW,
        )
        confianzaValor.insert(tk.END, str(self.regla.confianza))
        confianzaValor.configure(state=tk.DISABLED, **
                          style.STYLE_TEXT, relief=tk.GROOVE,)

        tpr = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        tpr.grid(
            row=8,
            column=0,
            sticky=tk.NSEW,
        )
        tpr.insert(tk.END, "True positive rate (TPr)")
        tpr.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        tprValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        tprValor.grid(
            row=9,
            column=0,
            sticky=tk.NSEW,
        )
        tprValor.insert(tk.END, str(self.regla.tpr))
        tprValor.configure(state=tk.DISABLED, **
                          style.STYLE_TEXT, relief=tk.GROOVE,)

        Wracc = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
            width=40,
        )
        Wracc.grid(
            row=6,
            column=1,
            sticky=tk.NSEW,
        )
        Wracc.insert(tk.END, "WRAccN")
        Wracc.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        WraccValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        WraccValor.grid(
            row=7,
            column=1,
            sticky=tk.NSEW,
        )
        WraccValor.insert(tk.END, str(self.regla.WRAccN))
        WraccValor.configure(state=tk.DISABLED, **
                          style.STYLE_TEXT, relief=tk.GROOVE,)

        fpr = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        fpr.grid(
            row=8,
            column=1,
            sticky=tk.NSEW,
        )
        fpr.insert(tk.END, "False negative rate (FPr)")
        fpr.configure(state=tk.DISABLED, **
                     style.STYLE_TITULO_TABLA, relief=tk.GROOVE,)

        fprValor = tk.Entry(
            infoReglaFrame,
            justify=tk.CENTER,
        )
        fprValor.grid(
            row=9,
            column=1,
            sticky=tk.NSEW,
        )
        fprValor.insert(tk.END, str(self.regla.fpr))
        fprValor.configure(state=tk.DISABLED, **
                          style.STYLE_TEXT, relief=tk.GROOVE,)
        
    def crearCabecera(self):
        inicioFrame = tk.Frame(self)
        inicioFrame.configure(background=style.COLOR_BACKGROUND,)
        inicioFrame.pack(
            side=tk.TOP,
            fill=tk.X,
            padx=20,
            pady=11,
        )

        tk.Button(
            inicioFrame,
            text=" ← Back",
            command=lambda: self.controller.get_frame("VisualizarReglas"),
            **style.STYLE_BUTTON,
            font=("Arial", 13)
        ).pack(
            side=tk.LEFT,
            padx=20,
            pady=11,
        )

        tk.Label(
            inicioFrame,
            text=self.regla.nombre,
            justify=tk.CENTER,
            wraplength=2000,
            **style.STYLE_TITULO_REGLAS  # Desenpaqueta STYLE,
        ).pack(
            fill=tk.X,
            padx=20,
            pady=11,
            side=tk.LEFT,
        )
    
    def frameDatos(self):
        infoReglaFrame = tk.Frame(self)
        infoReglaFrame.configure(background=style.COLOR_BACKGROUND,)
        infoReglaFrame.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            padx=20,
            expand=1,
        )
        infoReglaFrame.grid_columnconfigure(0, weight=1)
        infoReglaFrame.grid_rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(infoReglaFrame)

        scrollbar = tk.Scrollbar(
            infoReglaFrame, orient=tk.VERTICAL, command=self.canvas.yview)

        frame_canvas = tk.Frame(self.canvas)
        frame_canvas.configure(background=style.COLOR_BACKGROUND)
        frame_canvas.grid_columnconfigure(0, weight=1)
        frame_canvas.grid_columnconfigure(1, weight=1)
        self.canvas.create_window((0, 0), window=frame_canvas, anchor=tk.NW)
        
        self.canvas.bind('<Configure>', lambda e: frame_canvas.config(width=e.width))
        self.canvas.configure(yscrollcommand=scrollbar.set, background=style.COLOR_BACKGROUND,
                              borderwidth=0, highlightthickness=0)

        self.canvas.bind('<Configure>', lambda e: self.canvas
                         .configure(scrollregion=self.canvas.bbox(tk.ALL)))

        self.canvas.bind("<MouseWheel>", self.movement_mouse_wheel)
        self.canvas.bind("<Button-4>", self.movement_mouse_wheel)
        self.canvas.bind("<Button-5>", self.movement_mouse_wheel)
        

        self.canvas.grid(
            row=0,
            column=0,
            sticky=tk.NSEW,
            pady=20,
        )

        scrollbar.grid(
            row=0,
            column=1,
            sticky=tk.NS,
            pady=20,
        )

        return frame_canvas




    


