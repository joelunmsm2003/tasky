from django.conf.urls import patterns, include, url
from django.contrib.auth.models import Group, User
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView



admin.autodiscover()

urlpatterns = patterns('',


	#apis
	url(r'^ingresar$', 'ticket.apis.ingresar'),
	url(r'^envio/$', 'ticket.views.envio'),
	url(r'^enviolicencia/$', 'ticket.views.enviolicencia'),


	url(r'^admin/', include(admin.site.urls)),
 	url(r'^logeate/', 'ticket.views.logeate', name='reporte'),
 	url(r'^ticket/(\d+)/$', 'ticket.views.ticket'),


 	url(r'^chat1/$', 'ticket.views.chat1',name='chat1'),
 	url(r'^chat2/$', 'ticket.views.chat2',name='chat2'),
 	
	url(r'^chat/$', 'ticket.views.chat',name='chat'),

	url(r'^push$', 'ticket.views.push'),
	url(r'^push1$', 'ticket.views.push1'),

	url(r'^salir/', 'ticket.views.salir'),


	url(r'^cerrar/(\d+)/$', 'ticket.views.cerrar'),
	url(r'^validar/(\d+)/$', 'ticket.views.validar'),

	url(r'^reasignar_add/', 'ticket.views.reasignar_add'),
	url(r'^atender/(\d+)/$','ticket.views.atender'),
	url(r'^evento_add/(\d+)/$','ticket.views.evento_add'),
	url(r'^reasignar/(\d+)/(\d+)/$','ticket.views.reasignar'),


	
	url(r'^mdetalle_ticket/(\d+)/$','ticket.views.mdetalle_ticket'),

	url(r'^evento_add/', 'ticket.views.evento_add'),
	url(r'^eventos/(\d+)/$', 'ticket.views.eventos'),

	
	url(r'^ver_usuario/(\d+)/$', 'ticket.views.ver_usuario'),
	url(r'^add_tarea/$', 'ticket.views.add_tarea'),

	url(r'^agregar_ticket_movil/$', 'ticket.views.agregar_ticket_movil', name='agregar_ticket_movil'),

	url(r'^documentos/(\d+)/$', 'ticket.views.documentos'),
	url(r'^document_event/(\d+)/$', 'ticket.views.document_event'),
	url(r'^asignar_gilda/(\d+)/$','ticket.views.asignar_gilda'),
	url(r'^gilda/$','ticket.views.gilda'),
	url(r'^reasignar_gilda/(\d+)/$','ticket.views.reasignar_gilda'),
	url(r'^reasignar_post_gilda_new/(\d+)/(\d+)/(\d+)/$', 'ticket.views.reasignar_post_gilda_new'),
	url(r'^asignar_post_gilda_new/(\d+)/(\d+)/$', 'ticket.views.asignar_post_gilda_new'),

	url(r'^webx/','ticket.views.webx'),
	url(r'^email/','ticket.views.email'),
	url(r'^agregar_ticket_m/$','ticket.views.agregar_ticket_m'),
	url(r'^ticketscerrados/','ticket.views.ticketscerrados'),

	url(r'^apiticket/(\w+)/(\w+)','ticket.views.apiticket'),

	url(r'^telefono/(\w+)','ticket.views.telefono'),
	url(r'^eliminar_telefono/(\w+)','ticket.views.eliminar_telefono'),


	url(r'^agregar/','ticket.views.agregar'),
	url(r'^ver_ticket/','ticket.views.ver_ticket'),
  
	 
	url(r'^ticketopen/$','ticket.views.ticketopen'),

	url(r'^help/$','ticket.views.help'),
	url(r'^pantallas/$','ticket.views.pantallas'),
	url(r'^ttcerrados/', 'ticket.views.ttcerrados'),


	#Monitoreo


	url(r'^$', 'ticket.views.logeate'),
    url(r'^eliminar_parametro/(\w+)/(\w+)/(\w+)','monitoreo.views.eliminar_parametro'),
	url(r'^eliminar_equipo/(\w+)/(\w+)','monitoreo.views.eliminar_equipo'),
    url(r'^monitoreo/', 'monitoreo.views.empresa'),
    url(r'^equipo/(\w+)', 'monitoreo.views.equipo'),
   
    url(r'^parametro/(\w+)/(\w+)', 'monitoreo.views.parametro'),

    url(r'^editar_rango/(\w+)', 'monitoreo.views.editar_rango'),
    url(r'^editar_equipo/(\w+)', 'monitoreo.views.editar_equipo'),
    url(r'^editar_parametro/(\w+)', 'monitoreo.views.editar_parametro'),
    url(r'^rango/(\w+)', 'monitoreo.views.rango'),
    url(r'^eliminar_rango/(\w+)', 'monitoreo.views.eliminar_rango'),
    url(r'^maquinas/$', 'monitoreo.views.maquinas'),
    url(r'^equipote/(\w+)/$','monitoreo.views.equipote'),
    url(r'^equipos','monitoreo.views.equipos'),


    #index


    url(r'^sistema/$','monitoreo.views.sistema'),
    url(r'^login/$','monitoreo.views.login'),
    url(r'^input/$','monitoreo.views.input'),
    url(r'^version/$','monitoreo.views.version'),
    url(r'^salirsistema/', 'monitoreo.views.salirsistema'),
    url(r'^nequipos/', 'monitoreo.views.nequipos'),




)


