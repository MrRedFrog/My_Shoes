/* LOGIN NO LISTO*/
/*  rut: largo 9 a 10 caracteres
    nombre: largo 3 y 20
    apellido pat: largo 3 y 20 
    apellid mat: largo 3 y 20
    edad: entre 18 y 25 años 
    celular: largo entre 9 y 12 caracteres
*/
/* DECLARATION VAR*/

function validar(){
    var rut = document.getElementById("rut").value
    var nombre = document.getElementById("nombre").value
    var appat = document.getElementById("appat").value
    var apmat = document.getElementById("apmat").value
    var edad = document.getElementById("edad").value
    var celular = document.getElementById("celular").value

    if(rut.length >= 9 && rut.length <= 10){
        console.log("tu sistema de validacion funciona!")
        document.getElementById("rut").style.border = "1px solid lightgrey";
        if(nombre.length >= 3 && nombre.length <= 20){
            document.getElementById("nombre").style.border = "1px solid lightgrey";
            console.log("el nombre esta bien!")
            if(appat.length >= 3 && appat.length <= 20){
                console.log("el apellido esta bien!")
                document.getElementById("appat").style.border = "1px solid lightgrey"
                if(apmat.length >= 3 && apmat.length <= 20){
                    console.log("el apellido materno esta bien!")
                    document.getElementById("apmat").style.border = "1px solid lightgrey"
                    if(edad >= 18 && edad <= 25){
                        console.log("tienes la edad que corresponde!")
                        document.getElementById("edad").style.border = "1px solid lightgrey"
                        if(String(celular).length >= 9 && String(celular).length <= 12){
                            console.log("tu celular tiene el largo correspondiente!")
                            document.getElementById("celular").style.border = "1px solid lightgrey"
                            document.getElementById("resultado").innerHTML = "<div class='alert alert-success w-50 mx-auto text-center'>" +
                            "Campos validados correctamente!</div>"
                            return true;
                        }else{
                            console.log("tu celular debe tener un largo de 9 y 12 caracteres")
                            document.getElementById("celular").style.border = "1px solid red"
                            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                            "tu celular debe tener un largo de entre 9 y 12 caracteres</div>"
                        }        
                    }else{
                        console.log("tu edad debe ser entre 18 y 25 años")
                        document.getElementById("edad").style.border = "1px solid red"
                        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                        "tu edad debe ser entre 18 y 25 años para acceder!</div>"
                    }    
                }else{
                    console.log("el apellido materno debe tener entre 3 y 20 caracteres")
                    document.getElementById("apmat").style.border = "1px solid red"
                    document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                    "El apellido materno debe tener entre 3 y 20 caracteres </div>"
                }    
            }else{
                console.log("el apellido debe tener entre 3 y 20 caracteres")
                document.getElementById("appat").style.border = "1px solid red"
                document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
                "El apellido debe tener entre 3 y 20 caracteres</div>"
            }
        }else{
            console.log("el nombre debe tener entre 3 y 20 caracteres")
            document.getElementById("nombre").style.border = "1px solid red";
            document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
            "El nombre debe tener un largo de 3 y 20 caracteres</div>"
        }
    }else{ 
        console.log("tu sistema de validacion no funciona")
        document.getElementById("rut").style.border = "1px solid red";
        document.getElementById("resultado").innerHTML = "<div class='alert alert-danger w-50 mx-auto text-center'>" +
        "El rut debe tener un largo de 9 y 10 caracteres</div>"

    }
}
