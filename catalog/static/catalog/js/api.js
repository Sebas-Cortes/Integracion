$(document).ready(function () {
    var html = "<ul class='list-group'>";
    $.get("http://127.0.0.1:8000/api/Lote/", function(data){
        var direccion = data.direccion;
        var comuna = data.comuna;
        var lotes = data.lote;
        html += '<li class="list-group-item fs-3">Dirección: ' + direccion + '</li>';
        html += '<li class="list-group-item fs-3">Comuna: ' + comuna + '</li>';
            $.each(lotes ,function(i, item){
                html += '<li class="list-group-item">Tipo: ' + item.tipo + '</li>';
                html += '<li class="list-group-item">Cantidad: ' + item.cantidad + '</li>';
            });
            html += "</ul>";
            $("#cartas").append(html);
        });
});
