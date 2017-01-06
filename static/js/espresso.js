var defaultDrinks = [
	{name: "Latte", size_varieties: [
		{name: "Small", volume: 20}, {name: "Medium", volume: 40}, {name: "Large", volume: 60}
	]},
	{name: "Cappuccino", size_varieties: [
		{name: "Small", volume: 20}, {name: "Medium", volume: 40}, {name: "Large", volume: 60}
	]},
	{name: "Espresso", size_varieties: [
		{name: "Small", volume: 20}, {name: "Medium", volume: 40}, {name: "Large", volume: 60}
	]},
	{name: "Macchiato", size_varieties: [
		{name: "Small", volume: 20}, {name: "Medium", volume: 40}, {name: "Large", volume: 60}
	]},
	{name: "Extras", size_varieties: [
		{name: "1x shot", volume: 20}
	]}
];

var drinks = localStorage.getItem('drinks') ? JSON.parse(localStorage.getItem('drinks')) : defaultDrinks;

function buildTableBody (drinks) {

	var out = '';
	for (i in drinks) {
		for (j in drinks[i].size_varieties) {

			out += '<tr>';
			if (j == 0) out += '<td rowspan="' + drinks[i].size_varieties.length + '">' + drinks[i].name + '</td>';
			out += '<td>' + drinks[i].size_varieties[j].name + '</td><td><input type="number" class="form-control input-lg" name="' + drinks[i].name + '-' + drinks[i].size_varieties[j].name + '" value=' + drinks[i].size_varieties[j].volume + ' /></td></tr>';
		}
	}
	return out;
}

function storeDrinkVolumes () {

	for (i in drinks) {
		for (j in drinks[i].size_varieties) {

			drinks[i].size_varieties[j].volume = $('input[name="' + drinks[i].name + '-' + drinks[i].size_varieties[j].name + '"]').val();
		}
	}

	localStorage.setItem('drinks', JSON.stringify(drinks));

	window.location = '/';
}

function buildPanels (drinks) {

	var out = '';
	for (i in drinks) {
		out += '<div class="col-sm-6"><div class="panel panel-info"><div class="panel-heading"><h3 class="panel-title">' + drinks[i].name + '</h3></div><div class="panel-body">';
		for (j in drinks[i].size_varieties) {

			out += '<button class="btn btn-lg btn-default" data-volume=' + drinks[i].size_varieties[j].volume + '>' + drinks[i].size_varieties[j].name + '</button>';
		}
		out += '</div></div></div>';
	}
	return out;
}
