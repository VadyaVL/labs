REG.MODELS.Person = Backbone.Model.extend({
    urlRoot:"/api/v1/person",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var Person = Backbone.Collection.extend({
	model: REG.MODELS.Person,
	url : '/api/v1/person/',
});

REG.COLLECTIONS.Person = new Person;

REG.VIEWS.ExampleListItemPerson = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><b>Name:</b> <%- Name %> <b>Identification:</b> <%- Identification %> <b>NonResidentForeigner:</b> <%- NonResidentForeigner %></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deletePerson(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editPerson(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

function savePerson() {
    var model = null;
    if(document.forms.form[4].value>0) {
        model = new REG.MODELS.Address({id: document.forms.form[4].value});
        model.fetch({wait: true});
    }

    var person = new REG.MODELS.Person(   {Identification:document.forms.form[0].value,
                                            NonResidentForeigner:document.forms.form[1].checked,
                                            Name:document.forms.form[2].value,
                                            MoreInformation:document.forms.form[3].value,
                                            Address:model});
    person.save(null, {
          success: function(model, response){
            console.log('success');
            updView("Person");
          }
        });

      //  alert(stringify.toJSON(person));
    document.forms.form[0].value = "";
    document.forms.form[1].checked = false;
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
    document.forms.form[4].selectedIndex = 0;
};

function saveEPerson(i) {
    var adr = null;
    if(document.forms.form[4].value>0) {
        adr = new REG.MODELS.Address({id: document.forms.form[4].value});
        adr.fetch();
    }

     var model = REG.COLLECTIONS.Person.findWhere({id: i});
    model.save({Identification:document.forms.form[0].value,
                                            NonResidentForeigner:document.forms.form[1].checked,
                                            Name:document.forms.form[2].value,
                                            MoreInformation:document.forms.form[3].value,
                                            Address:adr},
            {
            type: 'PUT',
            success: function() {
                updView("Person");
            }
        });

    document.forms.form[0].value = "";
    document.forms.form[1].checked = false;
    document.forms.form[2].value = "";
    document.forms.form[3].value = "";
    document.forms.form[4].selectedIndex = 0;
};

function deletePerson(i) {
    var model = new REG.MODELS.Person({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("Person");
          }
        });
};

function editPerson(i) {
    var model = REG.COLLECTIONS.Person.findWhere({id: i});

    document.forms.form[0].value = model.get("Identification");
    document.forms.form[1].checked = model.get("NonResidentForeigner");
    document.forms.form[2].value = model.get("Name");
    document.forms.form[3].value = model.get("MoreInformation");
    if(model.get("Address")!=null)
    {
        var json = JSON.stringify(model.get("Address"));
        var jsonObj = JSON.parse(json);
        document.forms.form[4].value = jsonObj["id"];
    } else {
        document.forms.form[4].value = 0
    }
    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};
