<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;

/**
 * Class Postulacion
 *
 * @property $IdPostulacion
 * @property $FechaPostulacion
 * @property $DescripOferta
 * @property $PerfilPostulacion
 * @property $IdDetallesOferta
 * @property $IdEmpleado
 * @property $IdEstadoPostulaciones
 *
 * @property Agendamiento[] $agendamientos
 * @property Descripofertum $descripofertum
 * @property Empleado $empleado
 * @property Estadopostulacione $estadopostulacione
 * @package App
 * @mixin \Illuminate\Database\Eloquent\Builder
 */
class Postulacion extends Model
{
    protected $table = 'postulacion';

    static $rules = [
        'IdPostulacion' => 'required',
        'FechaPostulacion' => 'required',
        'DescripOferta' => 'required',
        'PerfilPostulacion' => 'required',
        'IdDetallesOferta' => 'required',
        'IdEmpleado' => 'required',
        'IdEstadoPostulaciones' => 'required',
    ];

    protected $perPage = 20;

    /**
     * Attributes that should be mass-assignable.
     *
     * @var array
     */
    protected $fillable = ['IdPostulacion', 'FechaPostulacion', 'DescripOferta', 'PerfilPostulacion', 'IdDetallesOferta', 'IdEmpleado', 'IdEstadoPostulaciones'];



    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasMany
     */
    public function agendamientos()
    {
        return $this->hasMany('App\Models\Agendamiento', 'IdPostulacion', 'IdPostulacion');
    }

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasOne
     */
    public function descripofertum()
    {
        return $this->hasOne('App\Models\Descripofertum', 'IdDetallesOferta', 'IdDetallesOferta');
    }

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasOne
     */
    public function empleado()
    {
        return $this->hasOne('App\Models\Empleado', 'IdEmpleado', 'IdEmpleado');
    }

    /**
     * @return \Illuminate\Database\Eloquent\Relations\HasOne
     */
    public function estadopostulacion()
    {
        return $this->hasOne('App\Models\Estadopostulacione', 'IdEstadoPostulaciones', 'IdEstadoPostulaciones');
    }
}