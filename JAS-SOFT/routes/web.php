<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/index', function () {
    return view("index");
});

Route::get('/insumos', function () {
    return view("insumos");
});

Route::get('/produccion', function () {
    return view("produccion");
});

Route::get('/insumos', function () {
    return view("insumos");
});

Route::get('/rrhh', function () {
    return view("rrhh");
});

Route::get('/ventas', function () {
    return view("ventas");
});

Route::get('/sales', function () {
    return view("sales");
});

Route::get('/inventario', function () {
    return view("inventario");
});

Route::get('/login', function () {
    return view("login");
});