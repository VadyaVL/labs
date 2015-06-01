REG.MODELS.TypeReg = Backbone.Model.extend({
    urlRoot:"/api/v1/typereg",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var TypeReg = Backbone.Collection.extend({
	model: REG.MODELS.TypeReg,
	url : '/api/v1/typereg',
});

REG.COLLECTIONS.TypeReg = new TypeReg;

REG.VIEWS.ExampleListItemTypeReg = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><b>Name:</b> <%- Name %></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deleteTypeReg(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editTypeReg(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function saveTypeReg() {
    var typeReg = new REG.MODELS.TypeReg({Name:document.forms.form[0].value});
    typeReg.save(null, {
          success: function(model, response){
            console.log('success');
            updView("TypeReg");
          }
        });
    document.forms.form[0].value = "";
};

function saveETypeReg(i) {
    var model = REG.COLLECTIONS.TypeReg.findWhere({id: i});
    model.save({Name:document.forms.form[0].value}, {
            type: 'PUT',
            success: function() {
                updView("TypeReg");
            }
        });
    document.forms.form[0].value = "";
};

function deleteTypeReg(i) {
    var model = new REG.MODELS.TypeReg({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("TypeReg");
          }
        });
};

function editTypeReg(i) {
    var model = REG.COLLECTIONS.TypeReg.findWhere({id: i});
    var elem = document.getElementById("id_Name");
    elem.value=model.get("Name");
    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};
