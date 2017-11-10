/**
 * Created by kevincastro on 10/29/17.
 */

//Side panel
$("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("active");
});

//Map inputs
$('#id_patient-map_0').attr('class','geoposition form-control');
$('#id_patient-map_1').attr('class','geoposition form-control');