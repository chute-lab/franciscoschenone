<template>

  <div id="app" class="container" >
    
  
    <div class="row">
      <div class="col-md-12">
        <h1></h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <formulario-persona @add-persona="agregarPersona" />
        <!-- <tabla-personas -->
        <!-- @delete-persona="eliminarPersona" -->
         <!-- v-bind:personas="personas"  -->
         
        
      </div>
    </div>
  </div>
</template>

<script>

// import TablaPersonas from './components/TablasPersonas.vue'
import FormularioPersona from './components/FormularioPersona.vue'


export default {
  name: 'App',
  components: {
    // TablaPersonas,
    FormularioPersona
  },
  data() {
  return {
  personas: [
{
id: 1,
nombre: '',
apellido: '',
numero: '',
email: '',
precioalerta: ''
},
],
}
},
methods: {
  agregarPersona(unapersona){
  let id = 0;
  if (this.personas.length > 0) {
  id = this.personas[this.personas.length - 1].id + 1;
  }
  this.personas= [...this.personas, { ...unapersona, id}];
},
eliminarPersona(idPersona){
  this.personas = this.personas.filter(
    persona => persona.id !== idPersona);
  
}
// conectarBarrio()
},
  
};
  

</script>

<style>
button {
  background: #009435;
  border: 1px solid #009435;
}
.colorfondo{
  background-color: rgb(255, 255, 255);

}
</style>






