var REG = {}
REG.MODELS = {}
REG.COLLECTIONS = {}
REG.VIEWS = {}


REG.MODELS.ViewEncModel = Backbone.Model.extend({
    urlRoot:"/api/v1/viewencumbrance",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});

var ViewOfEnc = Backbone.Collection.extend({
	model: REG.MODELS.ViewEncModel,
	url : '/api/v1/viewencumbrance',
});

REG.COLLECTIONS.ViewOfEnc = new ViewOfEnc;

REG.VIEWS.ExampleListItem = Backbone.View.extend({
	tagName : 'div',
	initialize : function(model, options){
		this.options = options
	},
	events : {
	},
	template : _.template("<div class=\"row\"><div class=\"col-md-6\"><b>Name:</b> <%- Name %></div><div class=\"col-md-6\"> <button class=\"btn\" onclick=\"deleteViewEnc(<%- id %> )\">Видалити</button><button class=\"btn\" onclick=\"editViewEnc(<%- id %> )\">Редагувати</button></div></div>"),
	render : function() {
		this.$el.html(this.template(this.model.toJSON()));
		return this;
	}
});

REG.VIEWS.ExampleList = Backbone.View.extend({
	el : "#my-model-list",
	whatIs: " ",
	initialize : function(options){
	},
	init : function(options){
        this.whatIs = options;
	    if(this.whatIs=="ViewEncumbrance"){
		    this.listenTo(REG.COLLECTIONS.ViewOfEnc, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="TypeOfEncumbrance"){
		    this.listenTo(REG.COLLECTIONS.TypeOfEnc, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="TypeReg"){
		    this.listenTo(REG.COLLECTIONS.TypeReg, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="TypeOfCurrency"){
		    this.listenTo(REG.COLLECTIONS.TypeOfCurrency, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="Address"){
		    this.listenTo(REG.COLLECTIONS.Address, 'reset', this.addAll, this);
		    }
		    else if(this.whatIs=="PAddress"){
		    this.listenTo(REG.COLLECTIONS.PAddress, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="Person"){
		    this.listenTo(REG.COLLECTIONS.Person, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="PPerson"){
		    this.listenTo(REG.COLLECTIONS.PPerson, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="PFormOfLeg"){
		    this.listenTo(REG.COLLECTIONS.PFormOfLeg, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="PTypeOfSocForm"){
		    this.listenTo(REG.COLLECTIONS.PTypeOfSocForm, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="PSocialFormation"){
		    this.listenTo(REG.COLLECTIONS.PSocialFormation, 'reset', this.addAll, this);
		    }
		   else if(this.whatIs=="PFilia"){
		    this.listenTo(REG.COLLECTIONS.PFilia, 'reset', this.addAll, this);
		    }




	},
	addOne : function(model) {
	    if(this.whatIs=="ViewEncumbrance"){
		    var view = new REG.VIEWS.ExampleListItem ({ model : model })
		}
		else if(this.whatIs=="TypeOfEncumbrance"){
		    var view = new REG.VIEWS.ExampleListItemTypeOfEnc ({ model : model })
		}
		else if(this.whatIs=="TypeReg"){
		    var view = new REG.VIEWS.ExampleListItemTypeReg ({ model : model })
		}
		else if(this.whatIs=="TypeOfCurrency"){
		    var view = new REG.VIEWS.ExampleListItemTypeOfCurrency ({ model : model })
		}
		else if(this.whatIs=="Address"){
		    var view = new REG.VIEWS.ExampleListItemAddress ({ model : model })
		}
		else if(this.whatIs=="PAddress"){
		    var view = new REG.VIEWS.ExampleListItemPAddress ({ model : model })
		}
		else if(this.whatIs=="Person"){
		    var view = new REG.VIEWS.ExampleListItemPerson ({ model : model })
		}
		else if(this.whatIs=="PPerson"){
		    var view = new REG.VIEWS.ExampleListItemPPerson ({ model : model })
		}
		else if(this.whatIs=="PFormOfLeg"){
		    var view = new REG.VIEWS.ExampleListItemPFormOfLeg ({ model : model })
		}
		else if(this.whatIs=="PTypeOfSocForm"){
		    var view = new REG.VIEWS.ExampleListItemPTypeOfSocForm ({ model : model })
		}
		else if(this.whatIs=="PSocialFormation"){
		    var view = new REG.VIEWS.ExampleListItemPSocialFormation ({ model : model })
		}
		else if(this.whatIs=="PFilia"){
		    var view = new REG.VIEWS.ExampleListItemPFilia ({ model : model })
		}

		this.$el.append(view.render().el)
	},
	addAll : function(){
		var that = this;
		if(this.whatIs=="ViewEncumbrance"){
            REG.COLLECTIONS.ViewOfEnc.each(function(model){
                that.addOne(model);
            });
		}
		else if(this.whatIs=="TypeOfEncumbrance"){
            REG.COLLECTIONS.TypeOfEnc.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="TypeReg"){
            REG.COLLECTIONS.TypeReg.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="TypeOfCurrency"){
            REG.COLLECTIONS.TypeOfCurrency.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="Address"){
            REG.COLLECTIONS.Address.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="PAddress"){
            REG.COLLECTIONS.PAddress.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="Person"){
            REG.COLLECTIONS.Person.each(function(model){
                that.addOne(model);
            });
            }
		 else if(this.whatIs=="PPerson"){
            REG.COLLECTIONS.PPerson.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="PFormOfLeg"){
            REG.COLLECTIONS.PFormOfLeg.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="PTypeOfSocForm"){
            REG.COLLECTIONS.PTypeOfSocForm.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="PSocialFormation"){
            REG.COLLECTIONS.PSocialFormation.each(function(model){
                that.addOne(model);
            });
		}
		 else if(this.whatIs=="PFilia"){
            REG.COLLECTIONS.PFilia.each(function(model){
                that.addOne(model);
            });
		}
	},
	remove: function() {
        this.$el.children().remove();
    },
	render : function() {
		this.$el.html(this.template());
		return this;
	}
});

function updView(options) {
    view.remove();

    if(options=="ViewEncumbrance"){
        REG.COLLECTIONS.ViewOfEnc.fetch({ reset : true });
    }
    else if(options=="TypeOfEncumbrance"){
        REG.COLLECTIONS.TypeOfEnc.fetch({ reset : true });
    }
    else if(options=="TypeReg"){
        REG.COLLECTIONS.TypeReg.fetch({ reset : true });
    }
    else if(options=="TypeOfCurrency"){
        REG.COLLECTIONS.TypeOfCurrency.fetch({ reset : true });
    }
    else if(options=="Address"){
        REG.COLLECTIONS.Address.fetch({ reset : true });
    }
    else if(options=="PAddress"){
        REG.COLLECTIONS.PAddress.fetch({ reset : true });
    }
    else if(options=="Person"){
        REG.COLLECTIONS.Person.fetch({ reset : true });
    }
    else if(options=="PPerson"){
        REG.COLLECTIONS.PPerson.fetch({ reset : true });
    }
    else if(options=="PFormOfLeg"){
        REG.COLLECTIONS.PFormOfLeg.fetch({ reset : true });
    }
    else if(options=="PTypeOfSocForm"){
        REG.COLLECTIONS.PTypeOfSocForm.fetch({ reset : true });
    }
    else if(options=="PSocialFormation"){
        REG.COLLECTIONS.PSocialFormation.fetch({ reset : true });
    }
    else if(options=="PFilia"){
        REG.COLLECTIONS.PFilia.fetch({ reset : true });
    }
};

function saveViewOfEnc() {
    var viewOfEnc = new REG.MODELS.ViewEncModel({Name:document.forms.form[0].value});
    viewOfEnc.save(null, {
          success: function(model, response){
            console.log('success');
            updView("ViewEncumbrance");
          }
        });
    document.forms.form[0].value = "";
};

function saveEViewOfEnc(i) {
    var model = REG.COLLECTIONS.ViewOfEnc.findWhere({id: i});
    model.save({Name:document.forms.form[0].value}, {
            type: 'PUT',
            success: function() {
                updView("ViewEncumbrance");
            }
        });
    document.forms.form[0].value = "";
};

function deleteViewEnc(i) {
    var model = new REG.MODELS.ViewEncModel({id: i});
    model.fetch();
    model.destroy({
          success: function(model, response){
            console.log('success');
            updView("ViewEncumbrance");
          }
        });
};

function editViewEnc(i) {
    var model = REG.COLLECTIONS.ViewOfEnc.findWhere({id: i});
    var elem = document.getElementById("id_Name");
    elem.value=model.get("Name");
    var str = "sendE(" + i + ")";
    var btn = document.getElementById("btn");
    btn.setAttribute("onclick", str);
    btn.value = "Редагувати";
};