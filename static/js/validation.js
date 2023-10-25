var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,4}$/;
var curpPattern = /^[A-Z]{1}[AEIOU]{1}[A-Z]{2}[0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])[HM]{1}[A-Z]{2}[BCDFGHJKLMNPQRSTVWXYZ]{3}[0-9A-Z]{1}[0-9]{1}$/;
 let valida_forma = () =>{
    let js_representante = getTextInputById("representante");
    let js_curp = getTextInputById("curp");
    let js_nombre = getTextInputById("nombre");
    let js_paterno = getTextInputById("paterno");
    let js_materno = getTextInputById("materno");
    let js_telefono = getTextInputById("telefono");
    let js_celular = getTextInputById("celular");
    let js_correo = getTextInputById("correo");
    let js_nivel = getTextInputById("nivel")
    let js_municipio = getTextInputById("municipio")
    let js_asunto = getTextInputById("asunto")

    if (js_representante.length == 0) {
        mensaje('error','Error Representante','Debe incluir el nombre de la persona que realizará el trámite',' ')
        return false;
    }
    else if (js_representante.length < 10){
        mensaje('error','Error','El nombre de la persona debe tener minimo 10 carácteres',null)
        return false;
    }
    else if (js_curp.length == 0) {
        mensaje('error','Curp Error','La CURP no puede ir vacía','')
        return false;
    }
    else if (js_curp.length != 18) {
        mensaje('error','Curp Error','La CURP debe contener 18 carácteres','')
        return false;
    }
    else if (!curpPattern.test(js_curp)){
        mensaje('error','Curp Error','Ingrese curp válido',null)
        return false;
    }
    else if (js_nombre.length == 0 ){
        mensaje('error','Nombre Error','El nombre no puede estar vacío',null)
        return false;
    }
    else if (js_nombre.length < 3 ){
        mensaje('error','Nombre Error','Ingrese un nombre válido',null)
        return false;
    }
    else if (js_paterno.length == 0 ){
        mensaje('error','Error Apellido Paterno','Debe agregar el apellido paterno',null)
        return false;
    }
    else if (js_paterno.length < 4 ){
        mensaje('error','Error Apellido Paterno','Ingrese un apellido paterno válido',null)
        return false;
    }
    else if (js_materno.length == 0 ){
        mensaje('error','Error Apellido Materno','Debe agregar el apellido materno',null)
        return false;
    }
    else if (js_materno.length < 4 ){
        mensaje('error','Error Apellido Materno','Ingrese un apellido materno válido',null)
        return false;
    }
    else if (js_telefono.length == 0 ){
        mensaje('error','Error Teléfono','El teléfono no debe estar vacío',null)
        return false;
    }
    else if (js_telefono.length != 10  ){
        mensaje('error','Error Teléfono','Ingrese un número de teléfono válido',null)
        return false;
    }
    else if (js_celular.length == 0 ){
        mensaje('error','Error Celular','Ingrese un número de celular',null)
        return false;
    }
    else if (js_celular.length != 10  ){
        mensaje('error','Error Celular','Debe ser un número de celular válido',null)
        return false;
    }
    else if (!emailPattern.test(js_correo)){
        mensaje('error','Correo Error','Ingrese correo válido',null)
        return false;
    }
    else if (js_nivel==0){
        mensaje('error','Error Nivel','Seleccione el nivel educativo ',null)
        return false;
    }
    else if (js_municipio==0){
        mensaje('error','Error municipio','Debe elegir un municipio ',null)
        return false;
    }
    else if (js_asunto==0){
        mensaje('error','Error Asunto','Seleccione un asunto ',null)
        return false;
    }

 }

 let getTextInputById = (id) =>{
    return document.getElementById(id).value.trim();
 }
 
 let mensaje = (tipo,titulo,texto,liga) =>{
  Swal.fire({
    type: tipo,
    title: titulo,
    text: texto,
    footer: liga
  });
 }