# 1. NÚCLEO DE LÓGICA RECURSIVA 
def calcular_recaudo_diario(lista_vehiculos):
    if len(lista_vehiculos) == 0:
        return 0
    return lista_vehiculos[0]["tarifa"] + calcular_recaudo_diario(lista_vehiculos[1:])

def buscar_vehiculo_por_placa(lista_vehiculos, placa_buscada):
    if len(lista_vehiculos) == 0:
        return False
    if lista_vehiculos[0]["placa"] == placa_buscada:
        return True
    return buscar_vehiculo_por_placa(lista_vehiculos[1:], placa_buscada)

def contar_vehiculos_categoria(lista_vehiculos, categoria):
    if len(lista_vehiculos) == 0:
        return 0
    if lista_vehiculos[0]["tipo"] == categoria:
        return 1 + contar_vehiculos_categoria(lista_vehiculos[1:], categoria)
    return contar_vehiculos_categoria(lista_vehiculos[1:], categoria)


# Costos fijos y almacenamiento del estado global
COSTO_LAVADO_MOTOR = 15000
COSTO_ENCERADO = 20000

lista_vehiculos = []

# Función auxiliar de presentación
def formatear_servicios_extra(vehiculo):
    servicios = []
    if vehiculo["motor"]: servicios.append("Lavado de motor")
    if vehiculo["encerado"]: servicios.append("Encerado")
    return ", ".join(servicios) if servicios else "Ninguno"


# 2. INTERFAZ GRÁFICA Y CONTROL DE VALIDACIONES INTEGRADO
import tkinter as tk
from tkinter import ttk, messagebox
import os

COLOR_FONDO = "#BDDBF9"
COLOR_PANEL = "#F8EEE4"
COLOR_ACENTO = "#4E97E0"
COLOR_ACENTO_HOVER = "#4697E2"
COLOR_TEXTO = "#1F3B57"
COLOR_ENCABEZADO = "#E7D5C3"

class AutolavadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autolavado y Detallado 'Rápido y Limpio'")
        self.root.geometry("900x800") 
        self.root.resizable(False, False)
        self.root.configure(bg=COLOR_FONDO)

        self._configurar_estilos()
        self._crear_widgets()

    def _configurar_estilos(self):
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("TFrame", background=COLOR_FONDO)
        style.configure("TLabelframe", background=COLOR_PANEL, bordercolor=COLOR_ACENTO, relief="groove")
        style.configure("TLabelframe.Label", background=COLOR_PANEL, foreground=COLOR_TEXTO, font=("Segoe UI", 10, "bold"))
        style.configure("TLabel", background=COLOR_PANEL, foreground=COLOR_TEXTO, font=("Segoe UI", 10))
        style.configure("TButton", background=COLOR_ACENTO, foreground="white", font=("Segoe UI", 10, "bold"), padding=6, borderwidth=0)
        style.map("TButton", background=[("active", COLOR_ACENTO_HOVER)])
        style.configure("TCheckbutton", background=COLOR_PANEL, foreground=COLOR_TEXTO, font=("Segoe UI", 10))
        style.map("TCheckbutton", background=[("active", COLOR_PANEL)])
        style.configure("TEntry", fieldbackground="white", foreground=COLOR_TEXTO)
        style.configure("TCombobox", fieldbackground="white", foreground=COLOR_TEXTO)
        style.configure("Treeview", background="white", fieldbackground="white", foreground=COLOR_TEXTO, rowheight=26)
        style.configure("Treeview.Heading", background=COLOR_ENCABEZADO, foreground=COLOR_TEXTO, font=("Segoe UI", 10, "bold"))
        style.map("Treeview", background=[("selected", COLOR_ACENTO)], foreground=[("selected", "white")])
        style.configure("Estado.TLabel", background=COLOR_ACENTO, foreground="white", font=("Segoe UI", 9))
  
    def _crear_widgets(self):
        frame_form = ttk.LabelFrame(self.root, text="Registro de Vehículo")
        frame_form.pack(fill="x", padx=10, pady=10)

        ttk.Label(frame_form, text="Placa:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_placa = ttk.Entry(frame_form, width=15)
        self.entry_placa.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(frame_form, text="Tipo de Vehículo:").grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.combo_tipo = ttk.Combobox(frame_form, values=["Automóvil", "Camioneta", "Moto"], state="readonly", width=13)
        self.combo_tipo.current(0)
        self.combo_tipo.grid(row=0, column=3, padx=5, pady=5)

        ttk.Label(frame_form, text="Tarifa ($):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_tarifa = ttk.Entry(frame_form, width=15)
        self.entry_tarifa.grid(row=1, column=1, padx=5, pady=5)

        frame_servicios = ttk.LabelFrame(frame_form, text="Servicios Adicionales")
        frame_servicios.grid(row=0, column=4, rowspan=2, padx=15, pady=5, sticky="nsew")

        self.var_motor = tk.BooleanVar()
        ttk.Checkbutton(frame_servicios, text=f"Lavado de Motor (+${COSTO_LAVADO_MOTOR})", variable=self.var_motor).pack(anchor="w", padx=8, pady=2)

        self.var_encerado = tk.BooleanVar()
        ttk.Checkbutton(frame_servicios, text=f"Encerado (+${COSTO_ENCERADO})", variable=self.var_encerado).pack(anchor="w", padx=8, pady=2)

        # SECCIÓN DEL LOGO AUTO-DETECTABLE
        ruta_script = os.path.dirname(os.path.abspath(__file__))
        ruta_logo_png = os.path.join(ruta_script, "logoAutolavado.png")

        if os.path.exists(ruta_logo_png):
            self.img_logo = tk.PhotoImage(file=ruta_logo_png)
            self.img_logo_sub = self.img_logo.subsample(4, 4) 
            label_logo = tk.Label(frame_form, image=self.img_logo_sub, bg=COLOR_PANEL)
            label_logo.grid(row=0, column=5, rowspan=2, padx=30, pady=5, sticky="e")

        frame_botones = ttk.Frame(self.root)
        frame_botones.pack(fill="x", padx=10, pady=5)

        ttk.Button(frame_botones, text="Registrar Vehículo", command=self.registrar_vehiculo).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Buscar Placa", command=self.buscar_placa).pack(side="left", padx=5)
        ttk.Button(frame_botones, text="Cerrar Jornada", command=self.cerrar_jornada).pack(side="left", padx=5)

        frame_tree = ttk.LabelFrame(self.root, text="Vehículos en Bahía / Lavados del Día")
        frame_tree.pack(fill="both", expand=True, padx=10, pady=10)

        columnas = ("placa", "tipo", "tarifa", "servicios")
        self.tree = ttk.Treeview(frame_tree, columns=columnas, show="headings", height=12)
        self.tree.heading("placa", text="Placa")
        self.tree.heading("tipo", text="Tipo")
        self.tree.heading("tarifa", text="Tarifa ($)")
        self.tree.heading("servicios", text="Servicios Extra")

        self.tree.column("placa", width=120, anchor="center")
        self.tree.column("tipo", width=120, anchor="center")
        self.tree.column("tarifa", width=120, anchor="center")
        self.tree.column("servicios", width=220, anchor="center")
        self.tree.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(frame_tree, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.label_estado = ttk.Label(self.root, text="Listo.", anchor="w", style="Estado.TLabel")
        self.label_estado.pack(fill="x", side="bottom")

    # VALIDACIONES
    def registrar_vehiculo(self):
        placa = self.entry_placa.get().strip().upper()
        tarifa_texto = self.entry_tarifa.get().strip()
        tipo = self.combo_tipo.get()

        if placa == "" or tarifa_texto == "":
            messagebox.showwarning("Datos incompletos", "Debes ingresar placa y tarifa.")
            return

        try:
            tarifa = float(tarifa_texto)
        except ValueError:
            messagebox.showerror("Error", "La tarifa debe ser un número válido.")
            return

        if tarifa <= 0:
            messagebox.showerror("Error", "La tarifa debe ser un valor mayor a cero.")
            return

        if buscar_vehiculo_por_placa(lista_vehiculos, placa):
            messagebox.showwarning("Duplicado", f"La placa {placa} ya está registrada hoy.")
            return

        if self.var_motor.get(): tarifa += COSTO_LAVADO_MOTOR
        if self.var_encerado.get(): tarifa += COSTO_ENCERADO

        vehiculo = {
            "placa": placa,
            "tipo": tipo,
            "tarifa": tarifa,
            "motor": self.var_motor.get(),
            "encerado": self.var_encerado.get(),
        }
        lista_vehiculos.append(vehiculo)

        self.tree.insert(
            "", "end",
            values=(vehiculo["placa"], vehiculo["tipo"], f"${vehiculo['tarifa']:,}", formatear_servicios_extra(vehiculo))
        )

        self.label_estado.config(text=f"Vehículo {vehiculo['placa']} registrado correctamente.")

        self.entry_placa.delete(0, tk.END)
        self.entry_tarifa.delete(0, tk.END)
        self.var_motor.set(False)
        self.var_encerado.set(False)

    def buscar_placa(self):
        placa = self.entry_placa.get().strip().upper()
        if placa == "":
            messagebox.showwarning("Dato faltante", "Escribe una placa en el campo correspondiente.")
            return

        if buscar_vehiculo_por_placa(lista_vehiculos, placa):
            messagebox.showinfo("Resultado", f"La placa {placa} SÍ está registrada hoy.")
        else:
            messagebox.showinfo("Resultado", f"La placa {placa} NO se encuentra registrada.")

    def cerrar_jornada(self):
        if len(lista_vehiculos) == 0:
            messagebox.showinfo("Cierre de Jornada", "No se registraron vehículos hoy.")
            return

        total = calcular_recaudo_diario(lista_vehiculos)
        autos = contar_vehiculos_categoria(lista_vehiculos, "Automóvil")
        camionetas = contar_vehiculos_categoria(lista_vehiculos, "Camioneta")
        motos = contar_vehiculos_categoria(lista_vehiculos, "Moto")

        reporte = (
            f"REPORTE DE CIERRE DE JORNADA\n\n"
            f"Total de vehículos atendidos: {len(lista_vehiculos)}\n"
            f"  - Automóviles: {autos}\n"
            f"  - Camionetas: {camionetas}\n"
            f"  - Motos: {motos}\n\n"
            f"Recaudo total del día: ${total:,}"
        )
        messagebox.showinfo("Cierre de Jornada", reporte)

        lista_vehiculos.clear()
        for fila in self.tree.get_children():
            self.tree.delete(fila)
        self.label_estado.config(text="Jornada cerrada. Registro reiniciado.")

def main():
    # Convertidor automático interno para solucionar el entorno Linux/Mac
    ruta_script = os.path.dirname(os.path.abspath(__file__))
    orig = os.path.join(ruta_script, "logoAutolavado.jpeg")
    dest = os.path.join(ruta_script, "logoAutolavado.png")
    
    if os.path.exists(orig) and not os.path.exists(dest):
        try:
            from PIL import Image
            img = Image.open(orig)
            img.save(dest, "PNG")
        except ImportError:
            # Si no tienes PIL, el script te avisa qué comando usar
            print("\n[AVISO] Para ver la imagen ejecuta este comando en tu terminal primero:")
            print("pip install pillow\n")

    root = tk.Tk()
    app = AutolavadoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()