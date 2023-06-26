<?php

namespace App\Http\Controllers;

use App\Models\Postulacion;
use Illuminate\Http\Request;

class PostulacionController extends Controller
{
    public function index()
    {
        $postulaciones = Postulacion::all();

        return view('postulacion.index')->with('postulaciones', $postulaciones);
    }

    public function create()
    {
        return view('postulacion.create');
    }

    public function store(Request $request)
    {
        /*$validatedData = $request->validate([
            'fechapostulacion' => 'required',
            'descripofertas' => 'required',
            'perfilpostulacion' => 'required',
            'iddetallesoferta' => 'required',
            'idempleado' => 'required',
            'idestadopostulaciones' => 'required',
        ]);*/

        $postulaciones = new Postulacion;
        $postulaciones->FechaPostulacion = $request->input('fechapostulacion');
        $postulaciones->DescripOferta = $request->input('descripoferta');
        $postulaciones->PerfilPostulacion = $request->input('perfilpostulacion');
        $postulaciones->IdDetallesOferta = $request->input('iddetallesoferta');
        $postulaciones->IdEmpleado = $request->input('idempleado');
        $postulaciones->IdEstadoPostulaciones = $request->input('idestadopostulaciones');

        $postulaciones->save();

        return redirect()->route('postulacion.listar')->with('success', 'Postulacion creada correctamente');
    }
    /**
     * Display the specified resource.
     */
    public function show()
    {

    }

    public function update(Request $request)
    {
        $validatedData = $request->validate([
            'fechapostulacion' => 'required',
            'descripoferta' => 'required',
            'perfilpostulacion' => 'required',
        ]);

        $idPostulacion = $request->input('idpostulacion');
        $postulacion = Postulacion::find($idPostulacion);


        $postulacion->FechaPostulacion = $request->input('fechapostulacion');
        $postulacion->DescripOferta = $request->input('descripoferta');
        $postulacion->PerfilPostulacion = $request->input('perfilpostulacion');
        $postulacion->save();




        return redirect()->back()->with('error', 'No se encontró la postulacion');
    }

    public function edit(Request $request)
    {
        $idPostulacion = $request->input('idPostulacion');
        //dd($ordenpedidos);      
        $postulacion = Postulacion::find($idPostulacion);
        //dd($idordenpedido);
        return view('postulacion.edit')->with('postulacion', $postulacion);
    }

    public function destroy(Request $request)
    {
        $idPostulacion = $request->input('idpostulacion');
        $postulacion = Postulacion::find($idPostulacion);
        $postulacion->delete();
        return redirect()->back()->with('success', 'Postulacion eliminada con éxito');



    }
}