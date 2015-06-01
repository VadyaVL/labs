REG.MODELS.PTypeOfSocForm = Backbone.Model.extend({
    urlRoot:"http://127.0.0.1:9000/api/v1/typeofsocform/",
         schema: {
             id: 'Number',
             Name: 'Text'
         },
         defaults:{
        id:null
    },
    idAttribute: 'id',
    validate: function (attr) {
    }
});

var PTypeOfSocForm = Backbone.Collection.extend({
	model: REG.MODELS.PTypeOfSocForm,
	url : 'http://127.0.0.1:9000/api/v1/typeofsocform/',
});

REG.COLLECTIONS.PTypeOfSocForm = new PTypeOfSocForm;

REG.VIEWS.ExampleListItemPTypeOfSocForm = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>Name:</b> <%- Name %></tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePTypeOfSocForm(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPTypeOfSocForm(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePTypeOfSocForm() {

    var typeOfSocForm = new REG.MODELS.PTypeOfSocForm(   {Name:document.forms.form[0].value});
    typeOfSocForm.save(null, {
          type: 'POST',
          success: function(model, response){
            console.log('success');
            updView("PTypeOfSocForm");
          }
        });
    document.forms.form[0].value = "";
};

function savePETypeOfSocForm(i) {
    var model = REG.COLLECTIONS.PTypeOfSocForm.findWhere({id: i});
    model.save({Name:document.forms.form[0].value},
            {
            type: 'PUT',
            success: function() {
                updView("PTypeOfSocForm");
            }
        });
    document.forms.form[0].value = "";
};

function deletePTypeOfSocForm(i) {
    var model = new REG.MODELS.PTypeOfSocForm({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("PTypeOfSocForm");
          }
        });
};

function editPTypeOfSocForm(i) {
    var model = REG.COLLECTIONS.PTypeOfSocForm.findWhere({id: i});

    document.forms.form[0].value = model.get("Name");

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};

function initPTypeOfSocForm(){
    var div = document.getElementById("form");

    var input = new Array(  document.createElement("input") );
    input[0].id = "Name";
    input[0].name = "Name";
    input[0].maxLength = "45";
    input[0].type = "text";
    input[0].value = "Назва";


    div.appendChild(input[0]); //appendChild
};