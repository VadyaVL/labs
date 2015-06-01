REG.MODELS.TypeEncModel = Backbone.Model.extend({
    urlRoot:"/api/v1/typeofencumbrance",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var TypeOfEnc = Backbone.Collection.extend({
	model: REG.MODELS.TypeEncModel,
	url : '/api/v1/typeofencumbrance',
});

REG.COLLECTIONS.TypeOfEnc = new TypeOfEnc;

REG.VIEWS.ExampleListItemTypeOfEnc = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><b>Name:</b> <%- Name %></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deleteTypeEnc(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editTypeEnc(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function saveTypeOfEnc() {
    var typeEncModel = new REG.MODELS.TypeEncModel({Name:document.forms.form[0].value});
    typeEncModel.save(null, {
          success: function(model, response){
            console.log('success');
            updView("TypeOfEncumbrance");
          }
        });
    document.forms.form[0].value = "";
};

function saveETypeOfEnc(i) {
    var model = REG.COLLECTIONS.TypeOfEnc.findWhere({id: i});
    model.save({Name:document.forms.form[0].value}, {
            type: 'PUT',
            success: function() {
                updView("TypeOfEncumbrance");
            }
        });
    document.forms.form[0].value = "";
};

function deleteTypeEnc(i) {
    var model = new REG.MODELS.TypeEncModel({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("TypeOfEncumbrance");
          }
        });
};

function editTypeEnc(i) {
    var model = REG.COLLECTIONS.TypeOfEnc.findWhere({id: i});
    var elem = document.getElementById("id_Name");
    elem.value=model.get("Name");
    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};
