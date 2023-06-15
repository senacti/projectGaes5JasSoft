<?php

namespace App\Http\Controllers;

use App\Models\Insumo;
use Illuminate\Console\View\Components\Alert;
use Illuminate\Http\Request;

class InsumoController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $insumos = Insumo::all();
     //   dd($insumos);
        return view('insumo.index')->with('insumos',$insumos);
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        return view('insumo.create');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        
       // Validar los datos recibidos del formulario
        $validatedData = $request->validate([
        'NombreInsumo' => 'required',
        'Cantidad' => 'required',
        'Unidadmedida' => 'required',
        'Color' => 'required',
        'Tamaño' => 'required',
        ]);
        
        // Crear un nuevo modelo o utilizar un modelo existente para almacenar los datos en la base de datos
        
        $insumos = new Insumo;
        $insumos->Cantidad = $request->input('Cantidad');
        $insumos->Color = $request->input('Color');
        $insumos->IdEmpleado = '2';
        $insumos->IdUnidadMedida = 2;
        $insumos->IdNombreInsumo = 2;
        //dd($insumo);
        $insumos->save();

        // Redirigir a una página de éxito o mostrar un mensaje de éxito
        return redirect()->route('insumo.listar')->with('Insumo creado con');
    }

    /**
     * Display the specified resource.
     */
    public function show(Insumo $insumos)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Insumo $id)
    {
        $insumos = Insumo::find($id);
        return view('insumos.info', ['insumo' => $insumos]);
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Insumo $id)
    {
        $insumos = Insumo::find($id);
        $insumos->Cantidad = $request->input('Cantidad');
        $insumos->Color = $request->input('color');
        $insumos->update();
        return redirect()->route('insumo.index')->with('Insumo actulizado con exito');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Insumo $id)    
    {                    
        $insumos = Insumo::find($id)->delete();             
       // $insumos->delete();
        return redirect()->route('insumo.index')->with('Insumo eliminado con exito');
    }
}
