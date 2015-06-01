REG.MODELS.PPerson = Backbone.Model.extend({
    urlRoot:"http://127.0.0.1:9000/api/v1/person/",
         schema: {
             id: 'Number'
         },
         defaults:{
        id:null
    },
    idAttribute: 'id',
    validate: function (attr) {
    }
});

var PPerson = Backbone.Collection.extend({
	model: REG.MODELS.PPerson,
	url : 'http://127.0.0.1:9000/api/v1/person/',
});

REG.COLLECTIONS.PPerson = new PPerson;

REG.VIEWS.ExampleListItemPPerson = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>Name:</b> <%- Name %> <b>Surname:</b> <%- Surname %> <b>Phone:</b> <%- Phone %></tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePPerson(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPPerson(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePPerson() {

    var person = new REG.MODELS.PPerson(   {Name:document.forms.form[0].value,
                                            Surname:document.forms.form[1].value,
                                            Phone:document.forms.form[2].value});
    person.save(null, {
          type: 'POST',
          success: function(model, response){
            console.log('success');
            updView("PPerson");
          }
        });
    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
};

function savePEPerson(i) {
    var model = REG.COLLECTIONS.PPerson.findWhere({id: i});
    model.save({Name:document.forms.form[0].value,
                                            Surname:document.forms.form[1].value,
                                            Phone:document.forms.form[2].value},
            {
            type: 'PUT',
            success: function() {
                updView("PPerson");
            }
        });
    document.forms.form[0].value = "";
    document.forms.form[1].value = "";
    document.forms.form[2].value = "";
};

function deletePPerson(i) {
    var model = new REG.MODELS.PPerson({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("PPerson");
          }
        });
};

function editPPerson(i) {
    var model = REG.COLLECTIONS.PPerson.findWhere({id: i});

    document.forms.form[0].value = model.get("Name");
    document.forms.form[1].value = model.get("Surname");
    document.forms.form[2].value = model.get("Phone");

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};

function initPPersonFrom(){
    var div = document.getElementById("form");

    var input = new Array(  document.createElement("input"),document.createElement("input"),
                            document.createElement("input") );
    input[0].id = "Name";
    input[0].name = "Name";
    input[0].maxLength = "45";
    input[0].type = "text";
    input[0].value = "Name";

    input[1].id = "Surname";
    input[1].name = "Surname";
    input[1].maxLength = "45";
    input[1].type = "text";
    input[1].value = "Surname";

    input[2].id = "Phone";
    input[2].name = "Phone";
    input[2].maxLength = "45";
    input[2].type = "text";
    input[2].value = "Phone";

    div.appendChild(input[0]); //appendChild
    div.appendChild(input[1]); //appendChild
    div.appendChild(input[2]); //appendChild
};