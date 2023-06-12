<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">   

    <link rel="stylesheet" type="text/css" href="{{ asset ('css/Style.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset ('css/Header.css') }}">
    <link rel="stylesheet" type="text/css" href="{{ asset ('css/footer.css') }}">
    <link rel="stylesheet" href="{{ asset ('css/estilos-dash-admin.css') }}"> 
    
    <link href="{{ asset ('https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css') }}" rel="stylesheet">     
    <link rel="stylesheet" href="{{ asset('https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css')}}">  
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>

    <link  rel="shortcut icon" href="PICTURES/iconlogo.png">
    <title>PromoPlast | Insumo</title>

    <meta name="csrf-token" content="{{ csrf_token() }}">
    <title>{{ config('app.name', 'Laravel') }}</title>
    <!-- Fonts -->
    <link rel="dns-prefetch" href="//fonts.bunny.net">
    <link href="https://fonts.bunny.net/css?family=Nunito" rel="stylesheet">

    <!-- Scripts -->
    @vite(['resources/sass/app.scss', 'resources/js/app.js'])
  </head>

  <body>
  <header class="dash-menu">
    <img class="logo-dash-admin" src="pictures/logo.png" alt="logo">
    <a class="nav-link" href="{{ url('/index') }}">INICIO</a>
    <ul class="list-menu-ul">      
        <li class="list-menu-dash"> <img class="img-menu-dash" src="pictures/campana.png" alt="Campana"> </li>
        <li class="list-menu-dash"> Administrador (Administrador) </li>
        <div class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
          <a class="dropdown-item" href="{{ route('logout') }}"
             onclick="event.preventDefault();
                           document.getElementById('logout-form').submit();">
              {{ __('Cerrar sesion') }}
          </a>

          <form id="logout-form" action="{{ route('logout') }}" method="POST" class="d-none">
              @csrf
          </form>
      </div>
        <li class="list-menu-dash"> <img class="img-menu-dash-users" src="pictures/usuario.png" alt=""> </li>
    </ul>
  </header>

  <div class="container-fluid">
    <div class="row">
      <div class="col-2 barmenu">
        <h3 class="mt-4">PROMOPLAST</h3>
        <p></p>
        <ul class="nav nav-pills flex-column">
          <li class="nav-item">
            <a class="nav-link" href="{{ url('/dashboard') }}">MENU</a>
          </li>
          <li class="nav-item">
          <a class="nav-link" href="{{ url('/rrhh') }}">RRHH</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{ url('/produccion') }}">PRODUCCION</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{ url('/inventario') }}">INVENTARIO</a>
            
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{{ url('/ventas') }}">VENTAS</a>
          </li>
        </ul>        
      </div>
          <div class="col-10" id="contentd">
            <div class="card" id="cardash">
              <nav class="descrip-menu">
              <a class="message-ubication" href="{{ url('produccion') }}">PRODUCCION</a>      
              </nav>  
              <div class="container mt-3">
                <h2>INSUMOS</h2>
                <p></p>                      
                <table class="table table-striped" id="tablas">
                  <thead>
                    <tr>
                      <th>Codigo Insumo</th>                      
                      <th>Cantidad</th>
                      <th>Unidad de medida</th>   
                      <th>Color</th>
                      <th>tamaño</th> 
                      <th></th>            
                    </tr>
                  </thead>
                  <tbody>
                   @foreach($insumos as $insumo)
                    <tr>
                      <td scope="row">{{$insumo->IdInsumo}}</td>                                       
                      <td>{{$insumo->Cantidad}}</td>
                      <td>{{$insumo->IdUnidadMedida}}</td>
                      <td>{{$insumo->Color}}</td>
                      <td>{{--$insumo->Tamaño--}}</td>
                      <td>     
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#editar{{$insumo->id}}">Editar</button>                        
                        <form action="{{ route('insumo.destroy',$insumo->id) }}" method="POST">
                          @method('DELETE')
                          @csrf
                          <button type="submit" class="btn btn-danger" >Eliminar</button>
                      </form>                   
                      </td>                                            
                    </tr>                                         
                    @endforeach                
                  </tbody>
                </table>  
                <div class="d-flex justify-content-around bg mb-3">
                  @include('insumo.create')                
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#create">
                    Nuevo Insumo
                  </button>
                  <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#ordenModal">
                    Crear orden de compra
                  </button>                                  
                </div>             
              </div>
            </div>      
          </div>
        </div>
      </div> 
    <script src="{{ asset ('https://code.jquery.com/jquery-3.6.0.min.js')}}"></script>  
    <script type="text/javascript" src="{{ asset ('js/jquery.dataTables.min.js') }}"></script>
    <script type="text/javascript" src="{{ asset ('js/dataTables.bootstrap.min.js') }}"></script>
    <script src="{{ asset ('https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js') }}"></script>
    <script src="{{ asset ('https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js') }}"></script>
    <script>
      $(document).ready( function () {
      $('#tablas').DataTable();
      } );

      function probar() {
        alert('entra');
      }
    </script>
    
    </body>
</html>