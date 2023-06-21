$(document).ready(function () {
    $.get("http://127.0.0.1:8000/api/Lote/", function(data){
            $.each(data ,function(i, item){
                $("#cartas").append('<div class="card" style="width: 18rem;"><div class="card-body"><h5 class="card-title">'+ item.tipo +'</h5><p class="card-text">Cantidad: '+ item.cantidad +'</p></div></div></div>');
            });
        });
});
