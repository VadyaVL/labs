REG.MODELS.PFormOfLeg = Backbone.Model.extend({
    urlRoot:"http://127.0.0.1:9000/api/v1/formofleg/",
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

var PFormOfLeg = Backbone.Collection.extend({
	model: REG.MODELS.PFormOfLeg,
	url : 'http://127.0.0.1:9000/api/v1/formofleg/',
});

REG.COLLECTIONS.PFormOfLeg = new PFormOfLeg;

REG.VIEWS.ExampleListItemPFormOfLeg = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><tr><b>Name:</b> <%- Name %></tr></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePFormOfLeg(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPFormOfLeg(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePFormOfLeg() {

    var formOfLeg = new REG.MODELS.PFormOfLeg(   {Name:document.forms.form[0].value});
    formOfLeg.save(null, {
          type: 'POST',
          success: function(model, response){
            console.log('success');
            updView("PFormOfLeg");
          }
        });
    document.forms.form[0].value = "";
};

function savePEFormOfLeg(i) {
    var model = REG.COLLECTIONS.PFormOfLeg.findWhere({id: i});
    model.save({Name:document.forms.form[0].value},
            {
            type: 'PUT',
            success: function() {
                updView("PFormOfLeg");
            }
        });
    document.forms.form[0].value = "";
};

function deletePFormOfLeg(i) {
    var model = new REG.MODELS.PFormOfLeg({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("PFormOfLeg");
          }
        });
};

function editPFormOfLeg(i) {
    var model = REG.COLLECTIONS.PFormOfLeg.findWhere({id: i});

    document.forms.form[0].value = model.get("Name");

    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};

function initPFormOfLeg(){
    var div = document.getElementById("form");

    var input = new Array(  document.createElement("input") );
    input[0].id = "Name";
    input[0].name = "Name";
    input[0].maxLength = "45";
    input[0].type = "text";
    input[0].value = "Назва";


    div.appendChild(input[0]); //appendChild
};