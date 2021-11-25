<template>
<div  class="container">
<div class="row">
      <div class="col-lg-6 col-lg-4 text-left">
    <h4 > Queres ver precios por Metro cuadrado por Barrio en CABA? </h4>
<button class="btn btn-primary" v-on:click= "show = !show"> Ver precios </button>
</div>
        <div class="col-lg-6 col-lg-4 text-center">
          <!-- <button class="btn btn-primary" v-on:click= "show = !show"> Ver precios </button> -->
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d210146.68168877432!2d-58.573383207134555!3d-34.615743688997895!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x95bcca3b4ef90cbd%3A0xa0b3812e88e88e87!2sBuenos%20Aires%2C%20CABA!5e0!3m2!1ses-419!2sar!4v1637779039249!5m2!1ses-419!2sar"
           width="500" height="250" style="border:0;" allowfullscreen="" loading="lazy"></iframe>
</div>
          
</div>
</div>



    <div class="background">
        <div v-if= "show" class="container">
                
        
      <h4 id= 'viajando' >Selecciona el barrio para ver precios promedio por mt2</h4>
      
          <table class="table" >
            <thead class="thead-dark">
              <tr>
              
                <th scope="col">Barrio</th>
                <th scope="col">USD</th>
                
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><a class="navlink" @click="getAllData"> Almagro  </a></td>
                <td>{{precio_barrios.precio}}</td>
              </tr>
              <tr>
                <td><a class="navlink" @click="getAllData1"> Belgrano  </a></td>
                <td>{{precio_barrios1.precio}}</td>
              </tr>
              <tr>
                <td><a class="navlink" @click="getAllData2"> Monserrat  </a></td>
                <td>{{precio_barrios2.precio}}</td>
              </tr>
              <tr>
                <td><a class="navlink" @click="getAllData3"> Palermo  </a></td>
                <td>{{precio_barrios3.precio}}</td>
              </tr>
              <tr>
                <td><a class="navlink" @click="getAllData4"> Recoleta  </a></td>
                <td>{{precio_barrios4.precio}}</td>
              </tr>
              <tr>
                <td><a class="navlink" @click="getAllData5"> Villa Crespo  </a></td>
                <td>{{precio_barrios5.precio}}</td>
              </tr>
              
              
            </tbody>
          </table>
      </div>

        
      </div>
            <!-- </div> -->
    <hr>
    <h1 id= 'viajando'> Crea tu alerta</h1>
  <div id="formulario-persona">
    <form @submit.prevent="enviarFormulario" >
      <div class="container">
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <label>Nombre</label>
              <input 
              ref = "nombre"
              v-model="persona.nombre"
              type="text" 
              class="form-control"
              :class ="{'is-invalid': procesando && nombreInvalido }"
              @focus="resetEstado"
              @keypress="resetEstado"
              />
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Apellido</label>
              <input 
              v-model="persona.apellido" 
              type="text" 
              class="form-control"
              :class ="{'is-invalid': procesando && apellidoInvalido }"
               />
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Email</label>
              <input v-model="persona.email" 
              type="email" 
              class="form-control"
              :class ="{'is-invalid': procesando && emailInvalido }" 
              />
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Numero</label>
              <input v-model="persona.numero" 
              type="tel" 
              class="form-control"
              :class ="{'is-invalid': procesando && numeroInvalido }" 
              />
            </div>
          </div>
           <div class="col-md-4">
            <div class="form-group">
              <label>Precio alerta</label>
              <input 
              v-model="persona.precioalerta" 
              type="float" 
              class="form-control"
              :class ="{'is-invalid': procesando && numeroInvalido }"
               />
            </div>
          </div>
          <div class="col-md-4">
            <div class="form-group">
              <label>Link</label>
              <input @onblur = "refreshIframe"
              @onfocus ="refreshIframe"
              @onfocusout = "refresIframe"
              v-model="persona.link" 
              type="text" 
              class="form-control"
              :class ="{'is-invalid': procesando && linkInvalido }"
               />
            </div>
          </div>
        </div>
        <div class="row">
          <div class="col-md-4">
            <div class="form-group">
              <button class="btn btn-primary">Crea tu alerta</button>
            </div>
          </div>
        </div>
      </div>
    <div class="container">
      <div class="row">
        <div class="col-md-12">
          <div v-if="error && procesando" class="alert
          alert-danger" role="alert">
            Debes rellenar todos los campos!
          </div>
            <div v-if="correcto" class="alert alert-success" role="alert">
              Estamos trabajando en tu alerta! Si tu propiedad baja de precio recibiras un Whatsapp 😎
            </div>
            
        </div>
        
      </div>
    </div>

    </form>

    <!-- <div><button class="btn btn-primary" @click="getAllData" >
      get_barrios by this.axios </button>
                          </div> -->
    <!-- <div><button class="btn btn-primary" @click="refreshIframe" >
      Probando el link </button>
                          </div> -->
                          
  <!-- <div> {{precio_barrios.precio}} </div> -->
  <!-- <img  src= "https://http2.mlstatic.com/D_NQ_NP_645547-MLA48195737370_112021-O.webp"> -->
  <!-- <div> {{linktest}} </div> -->
  <!-- <iframe v-if="linktest" src= "{{linktest}}"
marginwidth="0" marginheight="0" name="ventana_iframe" scrolling="no" border="0" 
frameborder="0" width="100%" height="800">

</iframe> -->
  


  </div>
</template>


<script>




import axios from 'axios';

export default {
  name: "formulario-persona",
  data() {
    return {
      procesando: false,
      correcto: false,
      error: false,
      linktest:"",
      show: false,
      vue: {
        exp:null,
      },
      precio_barrios: {
        precio: ""

      },
      precio_barrios1: {
        precio: ""

      },
      precio_barrios2: {
        precio: ""

      },precio_barrios3: {
        precio: ""

      },precio_barrios4: {
        precio: ""

      },precio_barrios5: {
        precio: ""

      },
      persona: {
        nombre: "",
        apellido: "",
        email: "",
        precioalerta: "",
        link: "",
        numero: ""
      },
    }
    },
    
   


    methods: {
      refreshIframe(){
        this.linktest = this.persona.link
        console.log(this.linktest)

      },
        enviarFormulario() {
          this.procesando = true
          axios.post("http://127.0.0.1:4000/buscando ", this.persona)
          .then(data=>{
            console.log(data)
          })
          this.resetEstado();

        // Comprobamos la presencia de errores
        if (this.nombreInvalido || this.apellidoInvalido || this.emailInvalido || this.numeroInvalido || this.linkInvalido || this.numeroInvalido) {
          this.error = true;
        return;
        }

      this.$emit('add-persona', this.persona);
      this.$refs.nombre.focus()

        this.error = false;
        this.correcto = true;
        this.procesando = false;
        },
       async getAllData() { 
         try { const res = await axios.get("http://127.0.0.1:4000/barrios"); 
         console.log(res) 
         this.precio_barrios.precio = res.data
         } catch (err) {
            console.log(err) }

      },
      async getAllData1() { 
         try { const res = await axios.get("http://127.0.0.1:4000/barrios1"); 
         console.log(res) 
         this.precio_barrios1.precio = res.data
         } catch (err) {
            console.log(err) }

      },
      async getAllData2() { 
         try { const res = await axios.get("http://127.0.0.1:4000/barrios2"); 
         console.log(res) 
         this.precio_barrios2.precio = res.data
         } catch (err) {
            console.log(err) }

      },
      async getAllData3() { 
         try { const res = await axios.get("http://127.0.0.1:4000/barrios3"); 
         console.log(res) 
         this.precio_barrios3.precio = res.data
         } catch (err) {
            console.log(err) }

      },
      async getAllData4() { 
         try { const res = await axios.get("http://127.0.0.1:4000/barrios4"); 
         console.log(res) 
         this.precio_barrios4.precio = res.data
         } catch (err) {
            console.log(err) }

      },
      async getAllData5() { 
         try { const res = await axios.get("http://127.0.0.1:4000/barrios5"); 
         console.log(res) 
         this.precio_barrios5.precio = res.data
         } catch (err) {
            console.log(err) }

      },
      
    
        resetEstado(){
          this.correcto = false;
          this.error = false;
          this.procesando = true;
        },
        
        
    },
    
    computed: {
        nombreInvalido() {
      return this.persona.nombre.length < 1;
      },
      apellidoInvalido() {
      return this.persona.apellido.length < 1;
      },
      emailInvalido() {
      return this.persona.email.length < 1;
      },
      numeroInvalido() {
      return this.persona.numero.length < 1;
      },
      linkInvalido() {
      return this.persona.link.length < 1;
      },

    },
 }
 
    
</script>










<style scoped>
form {
  margin-bottom: 2rem;
}
</style>


