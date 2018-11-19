
$(function() {
	/** -----------------------------------------
	 * Modulo del Slider 
	 -------------------------------------------*/
	 var SliderModule = (function() {
	 	var pb = {};
	 	pb.el = $('#slider');
	 	pb.items = {
	 		panels: pb.el.find('.slider-wrapper > li'),
	 	}

	 	// Interval del Slider
	 	var SliderInterval,
	 		currentSlider = 0,
	 		nextSlider = 1,
	 		lengthSlider = pb.items.panels.length;

	 	// Constructor del Slider
	 	pb.init = function(settings) {
	 		this.settings = settings || {duration: 8000};
	 		var items = this.items,
	 			lengthPanels = items.panels.length,
	 			output = '';

	 		// Insertamos nuestros botones
	 		for(var i = 0; i < lengthPanels; i++) {
	 			if(i == 0) {
	 				output += '<li class="active"></li>';
	 			} else {
	 				output += '<li></li>';
	 			}
	 		}

	 		$('#control-buttons').html(output);

	 		// Activamos nuestro Slider
	 		activateSlider();
	 		// Eventos para los controles
	 		$('#control-buttons').on('click', 'li', function(e) {
	 			var $this = $(this);
	 			if(!(currentSlider === $this.index())) {
	 				changePanel($this.index());
	 			}
	 		});

	 	}

	 	// Funcion para activar el Slider
	 	var activateSlider = function() {
	 		SliderInterval = setInterval(pb.startSlider, pb.settings.duration);
	 	}

	 	// Funcion para la Animacion
	 	pb.startSlider = function() {
	 		var items = pb.items,
	 			controls = $('#control-buttons li');
	 		// Comprobamos si es el ultimo panel para reiniciar el conteo
	 		if(nextSlider >= lengthSlider) {
	 			nextSlider = 0;
	 			currentSlider = lengthSlider-1;
	 		}

	 		controls.removeClass('active').eq(nextSlider).addClass('active');
	 		items.panels.eq(currentSlider).fadeOut('slow');
	 		items.panels.eq(nextSlider).fadeIn('slow');

	 		// Actualizamos los datos del slider
	 		currentSlider = nextSlider;
	 		nextSlider += 1;
	 	}

	 	// Funcion para Cambiar de Panel con Los Controles
	 	var changePanel = function(id) {
	 		clearInterval(SliderInterval);
	 		var items = pb.items,
	 			controls = $('#control-buttons li');
	 		// Comprobamos si el ID esta disponible entre los paneles
	 		if(id >= lengthSlider) {
	 			id = 0;
	 		} else if(id < 0) {
	 			id = lengthSlider-1;
	 		}

	 		controls.removeClass('active').eq(id).addClass('active');
	 		items.panels.eq(currentSlider).fadeOut('slow');
	 		items.panels.eq(id).fadeIn('slow');

	 		// Volvemos a actualizar los datos del slider
	 		currentSlider = id;
	 		nextSlider = id+1;
	 		// Reactivamos nuestro slider
	 		activateSlider();
	 	}

		return pb;
	 }());

	 SliderModule.init({duration: 4000});

});














/*
class IndexForSiblings{
	static get (el){
		let children = el.parentNode.children;

		for (var i = 0; i<children.length; i++){
			let child = children[i];
			if (child == el) return i;
		}
	}
}

class Slider{

	constructor(selector, movimiento = true){
		this.move = this.move.bind(this);
		this.moveByButton = this.moveByButton.bind(this);
		this.slider = document.querySelector(selector);
		this.itemsCount = this.slider.querySelectorAll(".containerdos > *").length;
		this.interval = null;
		this.contador =  0;
		this.movimiento =  movimiento;
		this.start();
		
		this.buildControls();
		this.bindEvents();

	}

	start(){
		if (!this.movimiento) return;
		this.interval = window.setInterval(this.move,5000);
	
	}
	
	restart(){
		if (this.interval) window.clearInterval(this.interval);
		this.start();
	}

	bindEvents(){
		this.slider.querySelectorAll(".controlsdos li")
			.forEach(item => {
				item.addEventListener("click", this.moveByButton)

			});
	}

	moveByButton(ev){
	let index = IndexForSiblings.get(ev.currentTarget);
	this.contador = index;
	this.moveTo(index);
	this.restart();

	}

	buildControls(){
		for (var i = 0; i<this.itemsCount; i++){
			let control = document.createElement("li");

			if (i == 0) control.classList.add("active");
			this.slider.querySelector(".controlsdos ul").appendChild(control);
		}
	}

	move(){
		//let itemsCount = this.sliderdos.querySelectorAll(".containerdos > * ").length;
		//console.log(itemsCount);
		this.contador++;
		if (this.contador > this.itemsCount -1) this.contador = 0;
		this.moveTo(this.contador);

	}

	resetIndicator(){
		this.slider.querySelectorAll(".controlsdos li.active")
			.forEach(item => item.classList.remove("active"));
	}

	moveTo(index){
		let left = index * 100;
		this.resetIndicator();
		this.slider.querySelector(".controlsdos li:nth-child("+(index+1)+")").classList.add("active");

		this.slider.querySelector(".containerdos").style.left = "-"+left+"%";
	}

}



(function(){
	new Slider(".sliderdos", true);

})();

*/

/*

class IndexForSiblings{
	static get(el){
		let children = el.parentNode.children;

		for (var i = 0; i < children.length; i++) {
			let child = children [i];
			if(child == el ) return i;
		}
	}
}

class Slider{
	constructor(selector, movimiento=true){
		this.move =  this.move.bind(this);
		this.moveByButton =  this.moveByButton.bind(this);
		this.slider =  document.querySelector(selector);
		let itemsCount = this.slider.querySelectorAll(".containerdos > *").length;
		
		this.interval =  null;
		this.contador = 0;
		this.movimiento = movimiento;

		this.start();
		
		this.buildControls();
		this.bindEvents();
	}

	start(){
		if (!this.movimiento) return;
		this.interval = window.setInterval(this.move,1000);
	}

	restart(){
		if (this.interval) window.clearInterval(this.interval);
		this.start();
	}

	bindEvents(){
		this.slider.querySelectorAll(".controls li")
			.forEach(item => {
				item.addEventListener("click",this.moveByButton)
			});

	}

	moveByButton(ev){
		let index =  IndexForSiblings.get(ev.currentTarget);
		this.contador = index;
		this.moveTo(index);
		this.restart();
	}

	buildControls(){
		for (var i = 0; i < this.itemsCount; i++) {
			let control =  document.createElement("li");

			if (i == 0 ) control.classList.add("active");
			this.slider.querySelector(".controls ul").appendChild(control);
		}
	}

	move(){
		this.contador++;
		//this.moveTo(this.contador);
		if(this.contador > this.itemsCount -1) this.contador = 0;
		this.moveTo(this.contador);


	}

	resetIndicator(){
		this.slider.querySelectorAll(".controls li.active")
			.forEach(item => item.classList.remove("active"));
	}

	moveTo(index){
		let left = index * 100;
		this.resetIndicator();
		this.slider.querySelector(".controls li:nth-child("+(index+1)+")").classList.add("active");

		this.slider.querySelector(".containerdos").style.left = "-"+left+"%";
	}
}

(function(){

	new Slider(".sliderdos", true);

})();

*/