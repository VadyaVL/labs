REG.MODELS.TypeOfCurrency = Backbone.Model.extend({
  urlRoot:"/api/v1/typeofcurrency/",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var TypeOfCurrency = Backbone.Collection.extend({
	model: REG.MODELS.TypeOfCurrency,
	url : '/api/v1/typeofcurrency/',
});

REG.COLLECTIONS.TypeOfCurrency = new TypeOfCurrency;

REG.VIEWS.ExampleListItemTypeOfCurrency = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><b>Name:</b> <%- Name %></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deleteTypeOfCurrency(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editTypeOfCurrency(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function saveTypeOfCurrency() {
    var typeOfCurrency = new REG.MODELS.TypeOfCurrency({Name:document.forms.form[0].value});
    typeOfCurrency.save(null, {
          success: function(model, response){
            console.log('success');
            updView("TypeOfCurrency");
          }
        });
    document.forms.form[0].value = "";
};

function saveETypeOfCurrency(i) {
    var model = REG.COLLECTIONS.TypeOfCurrency.findWhere({id: i});
    model.save({Name:document.forms.form[0].value}, {
            type: 'PUT',
            success: function() {
                updView("TypeOfCurrency");
            }
        });
    document.forms.form[0].value = "";
};

function deleteTypeOfCurrency(i) {
    var model = new REG.MODELS.TypeOfCurrency({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("TypeOfCurrency");
          }
        });
};

function editTypeOfCurrency(i) {
    var model = REG.COLLECTIONS.TypeOfCurrency.findWhere({id: i});
    var elem = document.getElementById("id_Name");
    elem.value=model.get("Name");
    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};
