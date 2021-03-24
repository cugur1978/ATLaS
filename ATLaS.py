from tkinter import *
from tkinter import ttk
import pandas as pd


root = Tk()
root.title("Asistant Toolkit for Laboratory Solutions")
root.minsize(width=580, height=350)
root.config(padx=10, pady=10)


def percent_window_open():
    percent_window = Toplevel()
    percent_window.title("ATLaS")
    percent_window.minsize(width=530, height=650)
    percent_window.config(padx=10, pady=10)


    def percent_calculate_button_clicked():
        percent_calculate_text.delete("1.0", "end")
        result = (float(volume_input.get()) * float(percent_input.get())) / 100
        percent_calculate_text.insert(END, f">> {result} g must be weighed and completed to desired volume of {volume_input.get()} ml using desired solvent")


    def mv_calculate_button_clicked():
        mw_calculate_text.delete("1.0", "end")
        if float(wanted_percent_input.get()) >= float(dilution_original_input.get()):
            mw_calculate_text.insert(END, "Desired concentration should not higher than or equal to stock concentration")
        else:
            result_mv = (float(wanted_volume_input.get()) * float(wanted_percent_input.get())) / float(dilution_original_input.get())
            mw_calculate_text.insert(END, f">> {round(result_mv, 4)} ml must be taken and completed to desired volume of {wanted_volume_input.get()} ml using desired solvent")


    def percent2molar_calculate_button_clicked():
        percent2molar_calculate_text.delete("1.0", "end")
        result_p2m = ((float(percent2molar_original_input.get())) * 10) / float(fw_chemical_input.get())
        percent2molar_calculate_text.insert(END, f">> The molarity of solution is {round(result_p2m, 4)}")



    main_label = Label(percent_window, text="PERCENT SOLUTIONS", fg="blue", font=("Arial", 15, "bold"))
    main_label.place(x=0, y=0)

#TEXT BOXES

    percent_calculate_text = Text(percent_window, width=70, height=3)
    percent_calculate_text.place(x=0, y=165)
    percent_calculate_text.configure(font=("Arial", 10))

    mw_calculate_text = Text(percent_window, width=70, height=3)
    mw_calculate_text.place(x=0, y=385)
    mw_calculate_text.configure(font=("Arial", 10))

    percent2molar_calculate_text = Text(percent_window, width=70, height=3)
    percent2molar_calculate_text.place(x=0, y=575)
    percent2molar_calculate_text.configure(font=("Arial", 10))


    # PERCENTAGE SOLUTION PREPARATION
    percent_main_label = Label(percent_window, text="Calculation of percent solutions", fg="orange",
                               font=("Arial", 12, "bold", "underline"))
    percent_main_label.place(x=0, y=40)

    percent_label = Label(percent_window, text="Enter desired percentage", font=("Arial", 10))
    percent_label.place(x=0, y=70)

    percent_input = Entry(percent_window)
    percent_input.place(x=200, y=70)
    percent_input.get()

    percent_symbol_label = Label(percent_window, text="%", font=("Arial", 10))
    percent_symbol_label.place(x=350, y=70)

    volume_label = Label(percent_window, text="Enter desired volume as ml", font=("Arial", 10))
    volume_label.place(x=0, y=100)

    volume_input = Entry(percent_window)
    volume_input.place(x=200, y=100)
    volume_input.get()

    volume_warning_label = Label(percent_window, text="(ml)", font=("Arial", 10))
    volume_warning_label.place(x=350, y=100)

    percent_calculate_button = Button(percent_window, text="Calculate", bg="green", fg="white",
                                      command=percent_calculate_button_clicked)
    percent_calculate_button.place(x=0, y=130)

    # DILUTION FROM PERCENT SOLUTION

    dilution_label = Label(percent_window, text="Dilution from percent solutions", fg="orange", font=("Arial", 12, "bold", "underline"))
    dilution_label.place(x=0, y=230)

    dilution_original_label = Label(percent_window, text="Concentration of stock sol.", font=("Arial", 10))
    dilution_original_label.place(x=0, y=260)

    dilution_original_input = Entry(percent_window)
    dilution_original_input.place(x=200, y=260)
    dilution_original_input.get()

    percent_symbol_label = Label(percent_window, text="%", font=("Arial", 10))
    percent_symbol_label.place(x=350, y=260)

    wanted_percent_label = Label(percent_window, text="Enter desired percentage", font=("Arial", 10))
    wanted_percent_label.place(x=0, y=290)

    wanted_percent_input = Entry(percent_window)
    wanted_percent_input.place(x=200, y=290)
    wanted_percent_input.get()

    percent_symbol_label = Label(percent_window, text="%", font=("Arial", 10))
    percent_symbol_label.place(x=350, y=290)

    wanted_volume_label = Label(percent_window, text="Enter desired volume as ml", font=("Arial", 10))
    wanted_volume_label.place(x=0, y=320)

    wanted_volume_input = Entry(percent_window)
    wanted_volume_input.place(x=200, y=320)
    wanted_volume_input.get()

    volume_warning_label = Label(percent_window, text="(ml)", font=("Arial", 10))
    volume_warning_label.place(x=350, y=320)

    mv_calculate_button = Button(percent_window, text="Calculate", bg="green", fg="white", command=mv_calculate_button_clicked)
    mv_calculate_button.place(x=0, y=350)

    # PERCENT TO MOLAR CALCULATION

    percent2molar_label = Label(percent_window, text="Calculation of percent to molar", fg="orange",
                                font=("Arial", 12, "bold", "underline"))
    percent2molar_label.place(x=0, y=450)

    percent2molar_original_label = Label(percent_window, text="Concentration of percent sol.", font=("Arial", 10))
    percent2molar_original_label.place(x=0, y=480)

    percent2molar_original_input = Entry(percent_window)
    percent2molar_original_input.place(x=200, y=480)
    percent2molar_original_input.get()

    percent_symbol_label = Label(percent_window, text="%", font=("Arial", 10))
    percent_symbol_label.place(x=350, y=480)

    fw_chemical_label = Label(percent_window, text="Enter the FW of chemical", font=("Arial", 10))
    fw_chemical_label.place(x=0, y=510)

    fw_chemical_input = Entry(percent_window)
    fw_chemical_input.place(x=200, y=510)
    fw_chemical_input.get()

    fw_chemical_symbol_label = Label(percent_window, text="g/mol", font=("Arial", 10))
    fw_chemical_symbol_label.place(x=350, y=510)

    percent2molar_calculate_button = Button(percent_window, text="Calculate", bg="green", fg="white",
                                            command=percent2molar_calculate_button_clicked)
    percent2molar_calculate_button.place(x=0, y=540)

def molar_window_open():
    molar_window = Toplevel()
    molar_window.title("ATLaS")
    molar_window.minsize(width=550, height=680)
    molar_window.config(padx=10, pady=10)

    def molar_mass_calc_button():
        molar_fw_text.delete("1.0", "end")
        molar_mass_result = (float(molar_fw_input.get()) * (float(molar_volume1_label.get()) / 1000) * float(
            molar_conc1_label.get()))
        molar_fw_text.insert(END, f">> {round(molar_mass_result, 3)} g must be weighed and completed to desired volume of {molar_volume1_label.get()} ml using desired solvent")


    def molar_dilute_calculation():
        molar_dilute_text.delete("1.0", "end")
        if float(molar_dilute_conc_input.get()) >= float(molar_dilute_stock_input.get()):
            molar_dilute_text.insert(END, "Desired concentration should not higher than or equal to stock concentration")
        else:
            molar_dilute_result = (float(molar_dilute_conc_input.get()) * (
                    float(molar_dilute_volume_input.get()))) / float(molar_dilute_stock_input.get())
            molar_dilute_text.insert(END ,f">> {round(molar_dilute_result, 3)} ml must be taken and completed to desired volume of {molar_dilute_volume_input.get()} ml using desired solvent")


    def molar_percent_calc_button():
        molar_percent_text.delete("1.0", "end")
        molar_percent_result = (float(molar_percent_volume_input.get()) * float(molar_percent_stock_input.get())) / 10
        molar_percent_text.insert(END ,f">> The concentration of the solution is {round(molar_percent_result, 3)}%")


    main_label = Label(molar_window, text="MOLAR SOLUTIONS", fg="blue", font=("Arial", 15, "bold"))
    main_label.place(x=0, y=0)

    #TEXT BOXES

    molar_fw_text = Text(molar_window, width=75, height=3)
    molar_fw_text.place(x=0, y=195)
    molar_fw_text.configure(font=("Arial", 10))

    molar_dilute_text = Text(molar_window, width=75, height=3)
    molar_dilute_text.place(x=0, y=410)
    molar_dilute_text.configure(font=("Arial", 10))

    molar_percent_text = Text(molar_window, width=75, height=3)
    molar_percent_text.place(x=0, y=600)
    molar_percent_text.configure(font=("Arial", 10))





    # MOLAR MASS CALCULATION

    molar_main_label = Label(molar_window, text="Calculation of mass required for Molar solutions", fg="orange",
                             font=("Arial", 12, "bold", "underline"))
    molar_main_label.place(x=0, y=40)

    molar_fw_label = Label(molar_window, text="Enter the FW of chemical", font=("Arial", 10))
    molar_fw_label.place(x=0, y=70)

    molar_fw_input = Entry(molar_window)
    molar_fw_input.place(x=220, y=70)
    molar_fw_input.get()

    molar_fw_symbol_label = Label(molar_window, text="g/mol", font=("Arial", 10))
    molar_fw_symbol_label.place(x=350, y=70)

    ######################

    molar_volume1_label = Label(molar_window, text="Enter the desired volume as ml", font=("Arial", 10))
    molar_volume1_label.place(x=0, y=100)

    molar_volume1_label = Entry(molar_window)
    molar_volume1_label.place(x=220, y=100)
    molar_volume1_label.get()

    molar_volume1_label2 = Label(molar_window, text="(ml)", font=("Arial", 10))
    molar_volume1_label2.place(x=350, y=100)

    #####################

    molar_conc1_label = Label(molar_window, text="Enter desired concentration as M ", font=("Arial", 10))
    molar_conc1_label.place(x=0, y=130)

    molar_conc1_label = Entry(molar_window)
    molar_conc1_label.place(x=220, y=130)
    molar_conc1_label.get()

    molar_conc1_label2 = Label(molar_window, text="(M)", font=("Arial", 10))
    molar_conc1_label2.place(x=350, y=130)

    ####################

    molar_mass_calc_button = Button(molar_window, text="Calculate", bg="green", fg="white", command=molar_mass_calc_button)
    molar_mass_calc_button.place(x=0, y=160)

    ################################# MOLAR DILUTION CALCULATION ########################################

    molar_dilute_label = Label(molar_window, text="Dilution of solution of known molarity", fg="orange",
                               font=("Arial", 12, "bold", "underline"))
    molar_dilute_label.place(x=0, y=260)

    molar_dilute_stock = Label(molar_window, text="Enter Stock's concentration as M", font=("Arial", 10))
    molar_dilute_stock.place(x=0, y=290)

    molar_dilute_stock_input = Entry(molar_window)
    molar_dilute_stock_input.place(x=220, y=290)
    molar_dilute_stock_input.get()

    molar_dilute_stock_symbol_label = Label(molar_window, text="(M)", font=("Arial", 10))
    molar_dilute_stock_symbol_label.place(x=350, y=290)

    ######################
    molar_dilute_volume = Label(molar_window, text="Enter desired volume as ml", font=("Arial", 10))
    molar_dilute_volume.place(x=0, y=320)

    molar_dilute_volume_input = Entry(molar_window)
    molar_dilute_volume_input.place(x=220, y=320)
    molar_dilute_volume_input.get()

    molar_dilute_volume_symbol_label = Label(molar_window, text="(ml)", font=("Arial", 10))
    molar_dilute_volume_symbol_label.place(x=350, y=320)

    ######################
    molar_dilute_conc = Label(molar_window, text="Enter desired concentration as M", font=("Arial", 10))
    molar_dilute_conc.place(x=0, y=350)

    molar_dilute_conc_input = Entry(molar_window)
    molar_dilute_conc_input.place(x=220, y=350)
    molar_dilute_conc_input.get()

    molar_dilute_conc_symbol_label = Label(molar_window, text="(M)", font=("Arial", 10))
    molar_dilute_conc_symbol_label.place(x=350, y=350)

    ######################

    molar_dilute_calc_button = Button(molar_window, text="Calculate", bg="green", fg="white", command=molar_dilute_calculation)
    molar_dilute_calc_button.place(x=0, y=380)

    ################################# MOLAR TO PERCENT CALCULATION ########################################

    molar_percent_label = Label(molar_window, text="Molarity to Percent Calculation", fg="orange",
                                font=("Arial", 12, "bold", "underline"))
    molar_percent_label.place(x=0, y=480)

    molar_percent_stock = Label(molar_window, text="Enter the FW of chemical", font=("Arial", 10))
    molar_percent_stock.place(x=0, y=510)

    molar_percent_stock_input = Entry(molar_window)
    molar_percent_stock_input.place(x=220, y=510)
    molar_percent_stock_input.get()

    molar_percent_stock_symbol_label = Label(molar_window, text="(g/mole)", font=("Arial", 10))
    molar_percent_stock_symbol_label.place(x=350, y=510)

    ######################
    molar_percent_volume = Label(molar_window, text="Enter molarity of solution as M", font=("Arial", 10))
    molar_percent_volume.place(x=0, y=540)

    molar_percent_volume_input = Entry(molar_window)
    molar_percent_volume_input.place(x=220, y=540)
    molar_percent_volume_input.get()

    molar_percent_volume_symbol_label = Label(molar_window, text="(M)", font=("Arial", 10))
    molar_percent_volume_symbol_label.place(x=350, y=540)

    ######################

    molar_percent_calc_button = Button(molar_window, text="Calculate", bg="green", fg="white", command=molar_percent_calc_button)
    molar_percent_calc_button.place(x=0, y=570)


def acidbase_window_open():

    acid_base_window = Tk()
    acid_base_window.title("ATLaS")
    acid_base_window.minsize(width=650, height=450)
    acid_base_window.config(padx=20, pady=10)
    main_label_acidbase = Label(acid_base_window, text="ACID & BASE SOLUTIONS", fg="blue", font=("Arial", 15, "bold"))
    main_label_acidbase.place(x=0, y=0)
    acid_base_df = pd.read_excel("acid_base_table.xls")

    def molar_acidbase_calc():
        final_result.delete("1.0", "end")
        molar_acidbase_result = ((float(weight_percentage_entry.get()) * float(density_entry.get())) / float(
            formula_weight_entry.get())) * 10
        molar_acidbase_result2 = (
                    (float(desired_concentration_entry.get()) * float(desired_volume_entry.get())) / float(
                molar_acidbase_result))
        result_string_1 = str(f">> The concentration of your stock solution is {round(molar_acidbase_result, 3)} M.")
        result_string_2 = str(
            f">> Take {round(molar_acidbase_result2, 3)} ml from {round(molar_acidbase_result, 3)} M solution.")
        result_string_3 = str(
            f">> Slowly add {round(molar_acidbase_result2, 3)} ml to {float(desired_volume_entry.get()) / 4} ml dH2O.")
        result_string_4 = str(f">> Then adjust the final volume to {desired_volume_entry.get()} ml.")
        final_result.insert(END, f"""{result_string_1}
    {result_string_2} 
    {result_string_3}
    {result_string_4}""")

    def normal_acidbase_calc():
        final_result.delete("1.0", "end")
        molar_acidbase_result = ((float(weight_percentage_entry.get()) * float(density_entry.get())) / float(
            formula_weight_entry.get())) * 10
        molar_acidbase_result2 = (
                    (float(desired_concentration_entry.get()) * float(desired_volume_entry.get())) / float(
                molar_acidbase_result))
        result_string_1 = str(
            f">> The concentration of your solution is {round((molar_acidbase_result * int(equivalent_value_entry.get())), 3)} N.")
        result_string_2 = str(
            f">> Take {round(molar_acidbase_result2 / int(equivalent_value_entry.get()), 3)} ml from {round(molar_acidbase_result / int(equivalent_value_entry.get()), 3)} N solution.")
        result_string_3 = str(
            f">> Slowly add {round(molar_acidbase_result2 / int(equivalent_value_entry.get()), 3)} ml to {float(desired_volume_entry.get()) / 4} ml dH2O.")
        result_string_4 = str(f">> Then adjust the final volume to {desired_volume_entry.get()} ml.")
        final_result.insert(END, f"""{result_string_1}
    {result_string_2} 
    {result_string_3}
    {result_string_4}""")

    def acid_base_listbox_used(event):
        # Gets current selection from listbox
        selected_item = acid_base_listbox.get(acid_base_listbox.curselection())
        selected_entry.delete(0, END)
        selected_entry.insert(END, string=selected_item)
        formula_entry.delete(0, END)
        formula_weight_entry.delete(0, END)
        density_entry.delete(0, END)
        weight_percentage_entry.delete(0, END)
        desired_concentration_entry.delete(0, END)
        desired_volume_entry.delete(0, END)
        equivalent_value_entry.delete(0, END)
        final_result.delete("1.0", "end")
        for i in acid_base:
            if i == selected_item:
                index_acidbase = acid_base.index(i)
                acid_base_formul = acid_base_formula[index_acidbase]
                acid_base_forw = acid_base_fw[index_acidbase]
                equivalent_var = equivalent_value[index_acidbase]
                formula_entry.insert(END, string=acid_base_formul)
                formula_weight_entry.insert(END, string=str(acid_base_forw))
                equivalent_value_entry.insert(END, string=str(equivalent_var))

            else:
                continue

    my_frame_Acid = Frame(acid_base_window)

    acid_base_listbox_scroll_y = Scrollbar(my_frame_Acid)
    acid_base_listbox_scroll_y.pack(side=RIGHT, fill=Y)
    acid_base_listbox_scroll_x = Scrollbar(my_frame_Acid, orient=HORIZONTAL)
    acid_base_listbox_scroll_x.pack(side=BOTTOM, fill=X)

    acid_base_listbox = Listbox(my_frame_Acid, height=18, width=22, font=("Arial", 11), yscrollcommand=acid_base_listbox_scroll_y.set, xscrollcommand=acid_base_listbox_scroll_x.set)
    acid_base_listbox.pack()

    acid_base = acid_base_df['Name'].tolist()
    acid_base_formula = acid_base_df['Formula'].tolist()
    acid_base_fw = acid_base_df['FW'].tolist()
    equivalent_value = acid_base_df['Equivalent'].tolist()

    acid_base_listbox_scroll_y.config(command=acid_base_listbox.yview)
    acid_base_listbox_scroll_x.config(command=acid_base_listbox.yview)
    my_frame_Acid.place(x=0, y=70)

    for item in acid_base:
        acid_base_listbox.insert(acid_base.index(item), item)

    acid_base_choose_label = Label(acid_base_window, text="Select acid or base", fg="orange", font=("Arial", 12, "bold"))
    acid_base_choose_label.place(x=0, y=40)
    acid_base_listbox.bind("<<ListboxSelect>>", acid_base_listbox_used)
    #acid_base_listbox.place(x=0, y=70)

    formula_entry_label = Label(acid_base_window, text="Formula:", fg="red", font=("Arial", 11))
    formula_entry_label.place(x=200, y=100)
    formula_entry = Entry(acid_base_window, width=22)
    formula_entry.place(x=200, y=125)

    fw_entry_label = Label(acid_base_window, text="Formula weight:", fg="red", font=("Arial", 11))
    fw_entry_label.place(x=200, y=150)
    formula_weight_entry = Entry(acid_base_window, width=22)
    formula_weight_entry.get()
    formula_weight_entry.place(x=200, y=175)
    fw_entry_label2 = Label(acid_base_window, text="g/mol", font=("Arial", 11))
    fw_entry_label2.place(x=335, y=179)

    density_entry_label = Label(acid_base_window, text="Enter the density:", fg="red", font=("Arial", 11))
    density_entry_label.place(x=400, y=100)
    density_entry = Entry(acid_base_window, width=20)
    density_entry.get()
    density_entry.place(x=400, y=125)
    density_entry_label2 = Label(acid_base_window, text="g/ml", font=("Arial", 11))
    density_entry_label2.place(x=540, y=125)

    weight_percentage_label = Label(acid_base_window, text="Weight percentage:", fg="red", font=("Arial", 11))
    weight_percentage_label.place(x=400, y=150)
    weight_percentage_entry = Entry(acid_base_window, width=20)
    weight_percentage_entry.get()
    weight_percentage_entry.place(x=400, y=175)
    weight_percentage_label2 = Label(acid_base_window, text="% w/w", font=("Arial", 11))
    weight_percentage_label2.place(x=545, y=175)

    desired_volume_label = Label(acid_base_window, text="Enter desired volume as ml:", fg="red", font=("Arial", 11))
    desired_volume_label.place(x=400, y=200)
    desired_volume_entry = Entry(acid_base_window, width=20)
    desired_volume_entry.get()
    desired_volume_entry.place(x=400, y=225)
    desired_volume_label2 = Label(acid_base_window, text="ml", font=("Arial", 11))
    desired_volume_label2.place(x=545, y=225)

    desired_concentration_label = Label(acid_base_window, text="Enter desired concentration as M:", fg="red", font=("Arial", 11))
    desired_concentration_label.place(x=400, y=257)
    desired_concentration_entry = Entry(acid_base_window, width=20)
    desired_concentration_entry.get()
    desired_concentration_entry.place(x=400, y=285)
    desired_concentration_label2 = Label(acid_base_window, text="M / N", font=("Arial", 11))
    desired_concentration_label2.place(x=545, y=285)

    molar_acidbase_button = Button(acid_base_window, text="Molarity Calculation", bg="green", fg="white", command=molar_acidbase_calc)
    molar_acidbase_button.config(width=18)
    molar_acidbase_button.place(x=200, y=250)

    normal_acidbase_button = Button(acid_base_window, text="Normality Calculation", bg="blue", fg="white", command=normal_acidbase_calc)
    normal_acidbase_button.config(width=18)
    normal_acidbase_button.place(x=200, y=282)

    final_result = Text(acid_base_window, width=55, height=5)
    final_result.configure(font=("Arial", 10))
    final_result.place(x=200, y=313)

    equivalent_value_label = Label(acid_base_window, text="Equivalent", fg="red", font=("Arial", 11))
    equivalent_value_label.place(x=200, y=200)
    equivalent_value_entry = Entry(acid_base_window, width=22)
    equivalent_value_entry.get()
    equivalent_value_entry.place(x=200, y=225)

    selected_entry = Entry(acid_base_window, width=48)
    selected_entry.get()
    selected_entry.configure(font=("Arial", 11, "bold"))
    selected_entry.place(x=200, y=70)

def buffer_window_open():

    index_num = 0
    buffer_df = pd.read_excel("buffer_table.xls")

    def mass_calculation_bufferchem():
        result_bufferchem_text.delete("1.0", "end")
        mass_equation = float(desired_conc_bufferchem_entry.get()) * float(fw_bufferchem_entry.get()) * (
                    float(desired_volume_bufferchem_entry.get()) / 1000)
        buff_chem_result_string_1 = str(
            f">> To make a {desired_conc_bufferchem_entry.get()} M solution, add {round(mass_equation, 2)} g of {selected_item_bufferchem_entry.get()} to dH2O.")
        buff_chem_result_string_2 = str(
            f">> Adjust the final volume of the solution to {desired_volume_bufferchem_entry.get()} ml.")
        result_bufferchem_text.insert(END, f"""{buff_chem_result_string_1}   
    {buff_chem_result_string_2}""")

    def buffer_chem_listbox_used(event):
        selected_item = buffer_chem_listbox.get(buffer_chem_listbox.curselection())
        selected_item_bufferchem_entry.delete(0, END)
        selected_item_bufferchem_entry.insert(END, string=selected_item)
        fw_bufferchem_entry.delete(0, END)
        pka_bufferchem_entry.delete(0, END)
        phrange_bufferchem_entry.delete(0, END)
        result_bufferchem_text.delete("1.0", "end")
        for i in buffer_chem_list:
            if i == selected_item:
                buffer_chem_index = buffer_chem_list.index(i)
                buffer_chem_fw_selected = buffer_chem_fw_list[buffer_chem_index]
                buffer_chem_pKa_selected = buffer_chem_pKa_list[buffer_chem_index]
                buffer_chem_range_selected = buffer_chem_range_list[buffer_chem_index]
                fw_bufferchem_entry.insert(END, string=buffer_chem_fw_selected)
                pka_bufferchem_entry.insert(END, string=buffer_chem_pKa_selected)
                phrange_bufferchem_entry.insert(END, string=buffer_chem_range_selected)
            else:
                continue


    buffer_stock_window = Tk()
    buffer_stock_window.title("ATLaS")
    buffer_stock_window.minsize(width=560, height=460)
    buffer_stock_window.config(padx=20, pady=10)
    buffer_stock_window_label = Label(buffer_stock_window, text="BUFFER SOLUTIONS", fg="blue", font=("Arial", 15, "bold"))
    buffer_stock_window_label.place(x=0, y=0)
    buffer_stock_window.resizable(0, 0)

    my_frame = Frame(buffer_stock_window)

    buffer_chem_listbox_scroll_y = Scrollbar(my_frame)
    buffer_chem_listbox_scroll_y.pack(side=RIGHT, fill=Y)
    buffer_chem_listbox_scroll_x = Scrollbar(my_frame, orient=HORIZONTAL)
    buffer_chem_listbox_scroll_x.pack(side=BOTTOM, fill=X)

    buffer_chem_listbox_label = Label(buffer_stock_window, text="Click on the list item:", fg="red", font=("Arial", 11, "bold"))
    buffer_chem_listbox_label.place(x=0, y=30)
    buffer_chem_listbox = Listbox(my_frame, height=16, width= 30, font=("Arial", 10), yscrollcommand=buffer_chem_listbox_scroll_y.set, xscrollcommand=buffer_chem_listbox_scroll_x.set)
    #buffer_chem_listbox.place(x=0, y=53)
    buffer_chem_listbox.pack()

    buffer_chem_listbox_scroll_y.config(command=buffer_chem_listbox.yview)
    buffer_chem_listbox_scroll_x.config(command=buffer_chem_listbox.xview)
    my_frame.place(x=0, y=53)

    buffer_chem_list = buffer_df['Buffer'].tolist()
    buffer_chem_fw_list = buffer_df['FW'].tolist()
    buffer_chem_pKa_list = buffer_df['pKa'].tolist()
    buffer_chem_range_list = buffer_df['pH_Range'].tolist()

    for item in buffer_chem_list:
        buffer_chem_listbox.insert(buffer_chem_list.index(item), item)

    buffer_chem_listbox.bind("<<ListboxSelect>>", buffer_chem_listbox_used)

    selected_item_bufferchem_entry = Entry(buffer_stock_window, width=45)
    selected_item_bufferchem_entry.place(x=240, y=53)

    fw_bufferchem_label = Label(buffer_stock_window, text="Formula weight:", fg="red", font=("Arial", 10))
    fw_bufferchem_label.place(x=240, y=80)
    fw_bufferchem_entry = Entry(buffer_stock_window, width=17)
    fw_bufferchem_entry.get()
    fw_bufferchem_entry.place(x=240, y=110)
    fw_bufferchem_label2 = Label(buffer_stock_window, text="g/mol", font=("Arial", 10))
    fw_bufferchem_label2.place(x=350, y=110)

    pka_bufferchem_label = Label(buffer_stock_window, text="pKa:", fg="red", font=("Arial", 10))
    pka_bufferchem_label.place(x=410, y=80)
    pka_bufferchem_entry = Entry(buffer_stock_window, width=17)
    pka_bufferchem_entry.get()
    pka_bufferchem_entry.place(x=410, y=110)

    phrange_bufferchem_label = Label(buffer_stock_window, text="pH Range:", fg="red", font=("Arial", 10))
    phrange_bufferchem_label.place(x=240, y=140)
    phrange_bufferchem_entry = Entry(buffer_stock_window, width=45)
    phrange_bufferchem_entry.get()
    phrange_bufferchem_entry.place(x=240, y=163)


    desired_volume_bufferchem_label = Label(buffer_stock_window, text="Enter desired volume as ml:", fg="red", font=("Arial", 10))
    desired_volume_bufferchem_label.place(x=240, y=200)
    desired_volume_bufferchem_entry = Entry(buffer_stock_window, width=35)
    desired_volume_bufferchem_entry.get()
    desired_volume_bufferchem_entry.place(x=240, y=222)
    desired_volume_bufferchem_label2 = Label(buffer_stock_window, text="ml", font=("Arial", 10))
    desired_volume_bufferchem_label2.place(x=460, y=222)

    desired_conc_bufferchem_label = Label(buffer_stock_window, text="Enter desired concentration as M:", fg="red", font=("Arial", 10))
    desired_conc_bufferchem_label.place(x=240, y=250)
    desired_conc_bufferchem_entry = Entry(buffer_stock_window, width=35)
    desired_conc_bufferchem_entry.get()
    desired_conc_bufferchem_entry.place(x=240, y=272)
    desired_conc_bufferchem_label2 = Label(buffer_stock_window, text="M", font=("Arial", 10))
    desired_conc_bufferchem_label2.place(x=460, y=272)

    mass_calc_bufferchem_button = Button(buffer_stock_window, text="Calculate Mass", fg="white", bg="purple", font=("Arial"),
                                         command=mass_calculation_bufferchem)
    mass_calc_bufferchem_button.config(width=30)
    mass_calc_bufferchem_button.place(x=240, y=300)

    result_bufferchem_text = Text(buffer_stock_window, width=73, height=5)
    result_bufferchem_text.configure(font=("Arial", 10))
    result_bufferchem_text.place(x=0, y=350)

    ########################### SECOND PART OF THIS MODULE ##############################################

    # Listbox for Buffers

    #listbox_buffer_names_label = Label(buffer_stock_window, text="Select the buffer in the list", fg="red", font=("Arial", 11, "bold"))
    #listbox_buffer_names_label.place(x=0, y=30)
    #listbox_buffer_names = Listbox(buffer_stock_window, width=27, height=14, font=("Arial", 10))
    #listbox_buffer_names.place(x=0, y=53)

    #listbox_buffer_names_list = ["Na-Phosphate Buffer", "HCl-KCl Buffer", "Glycine_HCl Buffer", "Phthalate-HCl Buffer", "Aconitate Buffer",
    #                             "Citrate Buffer", "Acetate Buffer", "Citrat-Phospate Buffer", "Succinate Buffer", "Phtalate-NaOH Buffer",
    #                             "Boric Acid-Borax Buffer", "Glycine-NaOH Buffer", "Borax-NaOH Buffer", "Carbonate-Bicarbonate Buffer"]

    #for item in listbox_buffer_names_list:
    #    listbox_buffer_names.insert(listbox_buffer_names_list.index(item), item)

    #listbox_buffer_names.bind("<<ListboxSelect>>", listbox_buffer_names_used)

    # Frame for Buffer Tables
    #excel_frame = LabelFrame(buffer_stock_window, text="Buffer Table", fg="red", font=("Arial", 11, "bold"))
    #excel_frame.place(x=203, y=30)
    #excel_frame.config(width=461, height=270)

    # Treeview Widget

    #buffer_table_tview = ttk.Treeview(excel_frame)
    #buffer_table_tview.place(relheight=1, relwidth=1)
    #buffer_table_tview_scroll_x = Scrollbar(buffer_table_tview, orient="horizontal", command=buffer_table_tview.xview)
    #buffer_table_tview_scroll_y = Scrollbar(buffer_table_tview, orient="vertical", command=buffer_table_tview.yview)
    #buffer_table_tview.configure(xscrollcommand=buffer_table_tview_scroll_x.set,
    #                             yscrollcommand=buffer_table_tview_scroll_y.set)
    #buffer_table_tview_scroll_x.pack(side="bottom", fill="x")
    #buffer_table_tview_scroll_y.pack(side="right", fill="y")

    #buffer_prep_info_text = Text(buffer_stock_window, width=95, height=10, font=("Arial", 10))
    #buffer_prep_info_text.place(x=0, y=300)

    #buffer_prep_explanation_list = []


def unit_converter_open():
    def units_listbox_used(event):
        selected_item = units_listbox.get(units_listbox.curselection())
        selected_unit_entry.delete(0, END)
        unit_firstlevel_entry2.delete(0, END)
        unit_secondlevel_entry2.delete(0, END)
        unit_thirdlevel_entry2.delete(0, END)
        unit_firstlevel_entry.delete(0, END)
        unit_secondlevel_entry.delete(0, END)
        unit_thirdlevel_entry.delete(0, END)
        unit_converter_button.config(state="disabled")
        unit_firstlevel_entry.config(state="disabled")
        unit_secondlevel_entry.config(state="disabled")
        unit_thirdlevel_entry.config(state="disabled")

        for i in units_list:
            if i == selected_item:
                index_units_list = units_list.index(i)
                unit_value = units_list[index_units_list]
                selected_unit_entry.insert(END, string=unit_value)
            else:
                continue
        if selected_item == "Volume":
            R1.config(text="Microliter")
            R2.config(text="Mililiter")
            R3.config(text="Litre")
            unit_firstlevel_entry2.config(state="normal")
            unit_firstlevel_entry2.insert(END, string="microliter")
            unit_secondlevel_entry2.config(state="normal")
            unit_secondlevel_entry2.insert(END, string="mililiter")
            unit_thirdlevel_entry2.config(state="normal")
            unit_thirdlevel_entry2.insert(END, string="liter")
        elif selected_item == "Mass":
            R1.config(text="Microgram")
            R2.config(text="Miligram")
            R3.config(text="Kilogram")
            unit_firstlevel_entry2.config(state="normal")
            unit_firstlevel_entry2.insert(END, string="microgram")
            unit_secondlevel_entry2.config(state="normal")
            unit_secondlevel_entry2.insert(END, string="miligram")
            unit_thirdlevel_entry2.config(state="normal")
            unit_thirdlevel_entry2.insert(END, string="kilogram")
        elif selected_item == "Density":
            R1.config(text="Microgr/ml")
            R2.config(text="Miligr/ml")
            R3.config(text="gram/Litre")
            unit_firstlevel_entry2.config(state="normal")
            unit_firstlevel_entry2.insert(END, string="microgram/ml")
            unit_secondlevel_entry2.config(state="normal")
            unit_secondlevel_entry2.insert(END, string="miligram/ml")
            unit_thirdlevel_entry2.config(state="normal")
            unit_thirdlevel_entry2.insert(END, string="gram/L")

    def sel():
        selection = var.get()
        cleardata()
        if selection == 1:
            unit_firstlevel_entry.config(state="normal")
            unit_secondlevel_entry.config(state="disabled")
            unit_thirdlevel_entry.config(state="disabled")
        elif selection == 2:
            unit_firstlevel_entry.config(state="disabled")
            unit_secondlevel_entry.config(state="normal")
            unit_thirdlevel_entry.config(state="disabled")
        else:
            unit_firstlevel_entry.config(state="disabled")
            unit_secondlevel_entry.config(state="disabled")
            unit_thirdlevel_entry.config(state="normal")

    def unit_calculate_button_clicked():
        unit_firstlevel_entry.config(state="normal")
        unit_secondlevel_entry.config(state="normal")
        unit_thirdlevel_entry.config(state="normal")
        clear_button.config(state="normal")

        if selected_unit_entry.get() == "Volume":
            if var.get() == 1:
                unit_secondlevel_entry.insert(END, string=str(float(unit_firstlevel_entry.get()) / 1000))
                unit_thirdlevel_entry.insert(END, string=str(float(unit_firstlevel_entry.get()) / 1000000))
            elif var.get() == 2:
                unit_firstlevel_entry.insert(END, string=str(float(unit_secondlevel_entry.get()) * 1000))
                unit_thirdlevel_entry.insert(END, string=str(float(unit_secondlevel_entry.get()) / 1000))
            else:
                unit_firstlevel_entry.insert(END, string=str(float(unit_thirdlevel_entry.get()) * 1000000))
                unit_secondlevel_entry.insert(END, string=str(float(unit_thirdlevel_entry.get()) * 1000))

        elif selected_unit_entry.get() == "Mass":
            if var.get() == 1:
                unit_secondlevel_entry.insert(END, string=str(float(unit_firstlevel_entry.get()) / 1000))
                unit_thirdlevel_entry.insert(END, string=str(float(unit_firstlevel_entry.get()) / 1000000))
            elif var.get() == 2:
                unit_firstlevel_entry.insert(END, string=str(float(unit_secondlevel_entry.get()) * 1000))
                unit_thirdlevel_entry.insert(END, string=str(float(unit_secondlevel_entry.get()) / 1000))
            else:
                unit_firstlevel_entry.insert(END, string=str(float(unit_thirdlevel_entry.get()) * 1000000))
                unit_secondlevel_entry.insert(END, string=str(float(unit_thirdlevel_entry.get()) * 1000))

        elif selected_unit_entry.get() == "Density":
            if var.get() == 1:
                unit_secondlevel_entry.insert(END, string=str(float(unit_firstlevel_entry.get()) / 1000))
                unit_thirdlevel_entry.insert(END, string=str(float(unit_firstlevel_entry.get()) / 1000))
            elif var.get() == 2:
                unit_firstlevel_entry.insert(END, string=str(float(unit_secondlevel_entry.get()) * 1000))
                unit_thirdlevel_entry.insert(END, string=str(float(unit_secondlevel_entry.get()) / 1))
            else:
                unit_firstlevel_entry.insert(END, string=str(float(unit_thirdlevel_entry.get()) * 1000))
                unit_secondlevel_entry.insert(END, string=str(float(unit_thirdlevel_entry.get()) * 1))

        else:
            pass

        unit_converter_button.config(text="Clear the form >>")
        unit_converter_button.config(state="disabled")

    def cleardata():
        unit_firstlevel_entry.delete(0, END)
        unit_secondlevel_entry.delete(0, END)
        unit_thirdlevel_entry.delete(0, END)
        unit_converter_button.config(text="Calculate")
        unit_converter_button.config(state="normal")
        clear_button.config(state="disabled")

        selection = var.get()
        if selection == 1:
            unit_firstlevel_entry.config(state="normal")
            unit_secondlevel_entry.config(state="disabled")
            unit_thirdlevel_entry.config(state="disabled")
        elif selection == 2:
            unit_firstlevel_entry.config(state="disabled")
            unit_secondlevel_entry.config(state="normal")
            unit_thirdlevel_entry.config(state="disabled")
        else:
            unit_firstlevel_entry.config(state="disabled")
            unit_secondlevel_entry.config(state="disabled")
            unit_thirdlevel_entry.config(state="normal")

    unit_converter_window = Tk()
    unit_converter_window.title("ATLaS")
    unit_converter_window.minsize(width=450, height=280)
    unit_converter_window.config(padx=13, pady=10)
    unit_converter_window.resizable(0, 0)

    radio_button_frame = LabelFrame(unit_converter_window, text="Select the option")
    radio_button_frame.place(x=130, y=75)
    radio_button_frame.config(width=280, height=40)

    unit_converter_mainlabel = Label(unit_converter_window, text="UNIT CONVERTER", fg="blue", font=("Arial", 15, "bold"))
    unit_converter_mainlabel.place(x=0, y=6)

    units_listbox = Listbox(unit_converter_window, width=15, height=11, font=("Arial", 11))
    units_listbox.place(x=0, y=45)
    units_list = ["Volume", "Mass", "Density"]

    for item in units_list:
        units_listbox.insert(units_list.index(item), item)

    units_listbox.bind("<<ListboxSelect>>", units_listbox_used)

    selected_unit_entry = Entry(unit_converter_window, width=30, font=("Arial", 12, "bold"))
    selected_unit_entry.place(x=130, y=45)
    selected_unit_entry.get()

    # Radiobutton
    var = IntVar(unit_converter_window)

    R1 = Radiobutton(radio_button_frame, text="Option 1", variable=var, value=1, command=sel)
    R1.grid(row=0, column=0)

    R2 = Radiobutton(radio_button_frame, text="Option 2", variable=var, value=2, command=sel)
    R2.grid(row=0, column=1)

    R3 = Radiobutton(radio_button_frame, text="Option 3", variable=var, value=3, command=sel)
    R3.grid(row=0, column=2)

    ###########ENTRY BOXES

    unit_firstlevel_entry = Entry(unit_converter_window, width=22, font=("Arial", 10,))
    unit_firstlevel_entry.place(x=130, y=125)
    unit_firstlevel_entry.get()
    unit_firstlevel_entry.config(state="disabled")

    unit_firstlevel_entry2 = Entry(unit_converter_window, width=15, font=("Arial", 10,))
    unit_firstlevel_entry2.place(x=294, y=125)
    unit_firstlevel_entry2.get()
    unit_firstlevel_entry2.config(state="disabled")

    unit_secondlevel_entry = Entry(unit_converter_window, width=22, font=("Arial", 10,))
    unit_secondlevel_entry.place(x=130, y=155)
    unit_secondlevel_entry.get()
    unit_secondlevel_entry.config(state="disabled")

    unit_secondlevel_entry2 = Entry(unit_converter_window, width=15, font=("Arial", 10,))
    unit_secondlevel_entry2.place(x=294, y=155)
    unit_secondlevel_entry2.get()
    unit_secondlevel_entry2.config(state="disabled")

    unit_thirdlevel_entry = Entry(unit_converter_window, width=22, font=("Arial", 10,))
    unit_thirdlevel_entry.place(x=130, y=185)
    unit_thirdlevel_entry.get()
    unit_thirdlevel_entry.config(state="disabled")

    unit_thirdlevel_entry2 = Entry(unit_converter_window, width=15, font=("Arial", 10,))
    unit_thirdlevel_entry2.place(x=294, y=185)
    unit_thirdlevel_entry2.get()
    unit_thirdlevel_entry2.config(state="disabled")

    unit_converter_button = Button(unit_converter_window, text="Calculate", fg="white", bg="orange", font=("Arial", 10, "bold"),
                                   command=unit_calculate_button_clicked)
    unit_converter_button.config(width=15)
    unit_converter_button.place(x=130, y=215)

    clear_button = Button(unit_converter_window, text="Clear", fg="white", bg="red", font=("Arial", 10, "bold"), command=cleardata)
    clear_button.config(state="disabled", width=15)
    clear_button.place(x=275, y=215)

def read_me_open():
    read_me_window = Tk()
    read_me_window.title("ATLaS")
    read_me_window.minsize(width=450, height=280)
    read_me_window.config(padx=13, pady=10)
    read_me_window.resizable(0, 0)

    read_me_mainlabel = Label(read_me_window, text="Important Warning", fg="blue", font=("Arial", 12, "bold"))
    read_me_mainlabel.place(x=0, y=8)

    warnings_label1 = Label(read_me_window, text="With decimals, you must use dot, not commas (eg: 0.5)")
    warnings_label1.place(x=0, y=38)
    warnings_label2 = Label(read_me_window, text="In order for the calculations to be correct, you must pay attention to the units.")
    warnings_label2.place(x=0, y=68)
    warnings_label3 = Label(read_me_window, text=">>You must enter the volume values in ml.")
    warnings_label3.place(x=10, y=98)
    warnings_label4 = Label(read_me_window, text=">>You must enter the molar values in molar units.")
    warnings_label4.place(x=10, y=128)


    about_label1 = Label(read_me_window, text="For citation: ")
    about_label1.place(x=0, y=168)
    about_label2 = Label(read_me_window, text="Comlekcioglu, U. and Comlekcioglu, N. 2021. ")
    about_label2.place(x=0, y=198)




sol2sol_label = Label(text="ATLaS - Asistant Toolkit for Laboratory Solutions", fg = "orange", font = ("Arial", 14, "bold"))
sol2sol_label.place(x = 6, y = 13)

percent_button = Button(root, text="Percent\n\nSolutions", bg="blue", fg="white", font=("Arial", 13, "bold"), command=percent_window_open)
percent_button.config(height=5, width = 15)
percent_button.place(x=10, y=70)

molar_button = Button(root, text="Molar\n\nSolutions", bg="blue", fg="white", font=("Arial", 13, "bold"), command=molar_window_open)
molar_button.config(height=5, width = 15)
molar_button.place(x=200, y=70)

acidbase_button = Button(root, text="Acid & Base\n\nSolutions", bg="blue", fg="white", font=("Arial", 13, "bold"), command=acidbase_window_open)
acidbase_button.config(height=5, width = 15)
acidbase_button.place(x=390, y=70)

buffer_button = Button(root, text="Buffer\n\nSolutions", bg="blue", fg="white", font=("Arial", 13, "bold"), command= buffer_window_open)
buffer_button.config(height=5, width = 15)
buffer_button.place(x=10, y=210)

unit_converter_button = Button(root, text="Unit\n\nConverter", bg="blue", fg="white", font=("Arial", 13, "bold"), command= unit_converter_open)
unit_converter_button.config(height=5, width = 15)
unit_converter_button.place(x=200, y=210)

read_me_button = Button(root, text="Read me", bg="blue", fg="white", font=("Arial", 13, "bold"), command= read_me_open)
read_me_button.config(height=5, width = 15)
read_me_button.place(x=390, y=210)

root.mainloop()

