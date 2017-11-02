-- MySQL dump 10.13  Distrib 5.5.43, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: tasky
-- ------------------------------------------------------
-- Server version	5.5.43-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
INSERT INTO `auth_group` VALUES (1,'Clientes'),(2,'Soporte');
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_0e939a4f` (`group_id`),
  KEY `auth_group_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_417f1b1c` (`content_type_id`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add empresa',7,'add_empresa'),(20,'Can change empresa',7,'change_empresa'),(21,'Can delete empresa',7,'delete_empresa'),(22,'Can add chat',8,'add_chat'),(23,'Can change chat',8,'change_chat'),(24,'Can delete chat',8,'delete_chat'),(25,'Can add user',9,'add_usuarios'),(26,'Can change user',9,'change_usuarios'),(27,'Can delete user',9,'delete_usuarios'),(28,'Can add telefono',10,'add_telefono'),(29,'Can change telefono',10,'change_telefono'),(30,'Can delete telefono',10,'delete_telefono'),(31,'Can add tipo',11,'add_tipo'),(32,'Can change tipo',11,'change_tipo'),(33,'Can delete tipo',11,'delete_tipo'),(34,'Can add estado',12,'add_estado'),(35,'Can change estado',12,'change_estado'),(36,'Can delete estado',12,'delete_estado'),(37,'Can add ticket',13,'add_ticket'),(38,'Can change ticket',13,'change_ticket'),(39,'Can delete ticket',13,'delete_ticket'),(40,'Can add soporte',14,'add_soporte'),(41,'Can change soporte',14,'change_soporte'),(42,'Can delete soporte',14,'delete_soporte'),(43,'Can add evento',15,'add_evento'),(44,'Can change evento',15,'change_evento'),(45,'Can delete evento',15,'delete_evento'),(46,'Can add notificaciones',16,'add_notificaciones'),(47,'Can change notificaciones',16,'change_notificaciones'),(48,'Can delete notificaciones',16,'delete_notificaciones'),(49,'Can add document_ event',17,'add_document_event'),(50,'Can change document_ event',17,'change_document_event'),(51,'Can delete document_ event',17,'delete_document_event'),(52,'Can add document',18,'add_document'),(53,'Can change document',18,'change_document'),(54,'Can delete document',18,'delete_document'),(55,'Can add archivo',19,'add_archivo'),(56,'Can change archivo',19,'change_archivo'),(57,'Can delete archivo',19,'delete_archivo'),(58,'Can add equipos',20,'add_equipos'),(59,'Can change equipos',20,'change_equipos'),(60,'Can delete equipos',20,'delete_equipos'),(61,'Can add parametro',21,'add_parametro'),(62,'Can change parametro',21,'change_parametro'),(63,'Can delete parametro',21,'delete_parametro'),(64,'Can add tipo',22,'add_tipo'),(65,'Can change tipo',22,'change_tipo'),(66,'Can delete tipo',22,'delete_tipo'),(67,'Can add caracteristica',23,'add_caracteristica'),(68,'Can change caracteristica',23,'change_caracteristica'),(69,'Can delete caracteristica',23,'delete_caracteristica'),(70,'Can add red',24,'add_red'),(71,'Can change red',24,'change_red'),(72,'Can delete red',24,'delete_red'),(73,'Can add rango',25,'add_rango'),(74,'Can change rango',25,'change_rango'),(75,'Can delete rango',25,'delete_rango');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$15000$qoMxJqfeSCHv$LiZ+cIcH8JqC0dwk0iE3eQV5+QwWf89n9j+eaQStrKM=','2015-11-30 15:59:55',1,'root','Root','','joelunmsm@gmail.com',1,1,'2015-11-30 13:18:34'),(2,'pbkdf2_sha256$15000$3iAeBif2rXpt$0/VnUbdCPsH6SLAoRtmZmcZlxNvKS5fCkTcqu0zVzlo=','2015-11-30 13:32:06',0,'xiencias','Xiencias','','joelunmsm@gmail.com',0,1,'2015-11-30 13:32:06'),(3,'pbkdf2_sha256$15000$07KgW1809h9t$VrGet6WZN4pJOslWgzjioh29RB9wNQadc3uHXK/nuHE=','2015-11-30 15:59:25',0,'mego','Mego Networks','','joelunmsm@gmail.com',0,1,'2015-11-30 13:32:29'),(4,'pbkdf2_sha256$15000$UQqJYWMbo1du$9WHF+VtCEcr9LUSDM0ce77SecnCu304VuU+o4oDayk0=','2015-11-30 13:32:56',0,'peruveloz','Peru Veloz','','joelunmsm@gmail.com',0,1,'2015-11-30 13:32:56'),(5,'pbkdf2_sha256$15000$NIbUWttzD9AC$+WHYB7XRc6zXHTfFjG85qq8jL50pT9cWv7A6bKD9JDU=','2015-11-30 13:33:43',0,'arzobizpadolima','Arzobispado de Lima','','joelunmsm@gmail.com',0,1,'2015-11-30 13:33:43'),(6,'pbkdf2_sha256$15000$brPxAQQa4F6o$Pm9k/erhogIFhzTvqLCrUEnUhdU3zvZy4wpIZiZaRF8=','2015-11-30 13:39:13',0,'alvaro','Alvaro','','',0,1,'2015-11-30 13:39:13'),(7,'pbkdf2_sha256$15000$S1hEDGdmJbGk$5CyfiQ7JaMheK15acJBUSexPwSilZmE1r2bU757Vtuk=','2015-11-30 14:57:01',0,'mayra','Mayra','','mayra@xiencias.org',0,1,'2015-11-30 14:57:01'),(8,'pbkdf2_sha256$15000$bWVfCql1rhCm$cDuvSj10jjIslO24lwGDtY+AqNBzVtriAWlbuxRx0fY=','2015-11-30 14:57:52',0,'joel','Joel','','joelunmsm@gmail.com',0,1,'2015-11-30 14:57:52'),(9,'pbkdf2_sha256$15000$iEzIRdGEkMiX$aO9/XOfWjC0+wZcchSvnO4o0Kqb0BlzanmouupgBQs8=','2015-11-30 15:27:17',0,'gila','Gila','','consultorasgg@yahoo.es',0,1,'2015-11-30 15:27:17');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_e8701ad4` (`user_id`),
  KEY `auth_user_groups_0e939a4f` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
INSERT INTO `auth_user_groups` VALUES (19,1,2),(20,2,2),(17,3,1),(18,4,1),(15,5,1),(6,6,2),(16,7,2),(14,8,2);
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_e8701ad4` (`user_id`),
  KEY `auth_user_user_permissions_8373b171` (`permission_id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_417f1b1c` (`content_type_id`),
  KEY `django_admin_log_e8701ad4` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2015-11-30 13:26:37','1','root',2,'Changed groups.',4,1),(2,'2015-11-30 13:32:06','2','xiencias',1,'',4,1),(3,'2015-11-30 13:32:18','2','xiencias',2,'Changed groups.',4,1),(4,'2015-11-30 13:32:30','3','mego',1,'',4,1),(5,'2015-11-30 13:32:43','3','mego',2,'Changed groups.',4,1),(6,'2015-11-30 13:32:56','4','peruveloz',1,'',4,1),(7,'2015-11-30 13:33:03','4','peruveloz',2,'Changed groups.',4,1),(8,'2015-11-30 13:33:43','5','arzobizpadolima',1,'',4,1),(9,'2015-11-30 13:33:52','5','arzobizpadolima',2,'Changed groups.',4,1),(10,'2015-11-30 13:39:13','6','alvaro',1,'',4,1),(11,'2015-11-30 13:39:24','6','alvaro',2,'Changed first_name and groups.',4,1),(12,'2015-11-30 13:55:29','3','mego',2,'Changed first_name.',4,1),(13,'2015-11-30 13:55:38','4','peruveloz',2,'Changed first_name.',4,1),(14,'2015-11-30 13:55:51','5','arzobizpadolima',2,'Changed first_name.',4,1),(15,'2015-11-30 13:56:11','2','xiencias',2,'Changed first_name.',4,1),(16,'2015-11-30 13:56:20','1','root',2,'Changed first_name.',4,1),(17,'2015-11-30 14:57:01','7','mayra',1,'',4,1),(18,'2015-11-30 14:57:40','7','mayra',2,'Changed first_name and groups.',4,1),(19,'2015-11-30 14:57:52','8','joel',1,'',4,1),(20,'2015-11-30 14:58:00','8','joel',2,'Changed first_name and groups.',4,1),(21,'2015-11-30 15:26:22','8','joel',2,'Changed email.',4,1),(22,'2015-11-30 15:27:18','9','gila',1,'',4,1),(23,'2015-11-30 15:56:07','5','arzobizpadolima',2,'Changed email.',4,1),(24,'2015-11-30 15:56:44','9','gila',2,'Changed email.',4,1),(25,'2015-11-30 15:57:11','7','mayra',2,'Changed email.',4,1),(26,'2015-11-30 15:57:32','3','mego',2,'Changed email.',4,1),(27,'2015-11-30 15:57:39','4','peruveloz',2,'Changed email.',4,1),(28,'2015-11-30 15:57:45','1','root',2,'Changed email.',4,1),(29,'2015-11-30 15:57:51','2','xiencias',2,'Changed email.',4,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'log entry','admin','logentry'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'empresa','ticket','empresa'),(8,'chat','ticket','chat'),(9,'user','ticket','usuarios'),(10,'telefono','ticket','telefono'),(11,'tipo','ticket','tipo'),(12,'estado','ticket','estado'),(13,'ticket','ticket','ticket'),(14,'soporte','ticket','soporte'),(15,'evento','ticket','evento'),(16,'notificaciones','ticket','notificaciones'),(17,'document_ event','ticket','document_event'),(18,'document','ticket','document'),(19,'archivo','ticket','archivo'),(20,'equipos','monitoreo','equipos'),(21,'parametro','monitoreo','parametro'),(22,'tipo','monitoreo','tipo'),(23,'caracteristica','monitoreo','caracteristica'),(24,'red','monitoreo','red'),(25,'rango','monitoreo','rango');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2015-11-30 13:17:23'),(2,'auth','0001_initial','2015-11-30 13:17:27'),(3,'admin','0001_initial','2015-11-30 13:17:28'),(4,'ticket','0001_initial','2015-11-30 13:17:37'),(5,'ticket','0002_document_asunto1','2015-11-30 13:17:38'),(6,'ticket','0003_auto_20141214_1413','2015-11-30 13:17:38'),(7,'ticket','0004_remove_document_asunto1','2015-11-30 13:17:38'),(8,'ticket','0005_document_asunto1','2015-11-30 13:17:39'),(9,'ticket','0006_auto_20141215_1934','2015-11-30 13:17:39'),(10,'ticket','0007_ticket_soporte_actual','2015-11-30 13:17:40'),(11,'ticket','0008_estadoobs_obs','2015-11-30 13:17:41'),(12,'ticket','0009_auto_20150121_1201','2015-11-30 13:17:42'),(13,'ticket','0010_authuser','2015-11-30 13:17:42'),(14,'ticket','0011_empresa','2015-11-30 13:17:43'),(15,'ticket','0012_auto_20150126_1620','2015-11-30 13:17:44'),(16,'ticket','0013_usuario','2015-11-30 13:17:44'),(17,'ticket','0014_usuarios','2015-11-30 13:17:45'),(18,'ticket','0015_auto_20150126_1724','2015-11-30 13:17:46'),(19,'ticket','0016_auto_20150126_1735','2015-11-30 13:17:49'),(20,'ticket','0017_auto_20150126_1809','2015-11-30 13:17:51'),(21,'ticket','0018_telefono_tipo','2015-11-30 13:17:51'),(22,'ticket','0019_auto_20150128_1551','2015-11-30 13:17:52'),(23,'ticket','0020_document_event','2015-11-30 13:17:54'),(24,'ticket','0021_auto_20150209_1127','2015-11-30 13:17:55'),(25,'ticket','0022_auto_20150216_1411','2015-11-30 13:17:56'),(26,'ticket','0023_telefono','2015-11-30 13:17:57'),(27,'ticket','0024_auto_20150217_1459','2015-11-30 13:17:58'),(28,'ticket','0025_auto_20150218_1445','2015-11-30 13:17:58'),(29,'monitoreo','0001_initial','2015-11-30 13:18:00'),(30,'monitoreo','0002_equipos_ip','2015-11-30 13:18:01'),(31,'monitoreo','0003_rango','2015-11-30 13:18:03'),(32,'monitoreo','0004_auto_20150218_1502','2015-11-30 13:18:05'),(33,'monitoreo','0005_auto_20150218_1527','2015-11-30 13:18:06'),(34,'sessions','0001_initial','2015-11-30 13:18:07'),(35,'ticket','0026_auto_20150426_1109','2015-11-30 13:18:09'),(36,'ticket','0027_chat','2015-11-30 13:18:11'),(37,'ticket','0028_auto_20150504_1205','2015-11-30 13:18:12'),(38,'ticket','0029_auto_20150504_1208','2015-11-30 13:18:13'),(39,'ticket','0030_chat_name','2015-11-30 13:18:15'),(40,'ticket','0031_ticket_empresa','2015-11-30 13:18:16'),(41,'ticket','0032_auto_20150526_1425','2015-11-30 13:18:18'),(42,'ticket','0033_auto_20150528_1705','2015-11-30 13:18:19'),(43,'ticket','0034_auto_20150528_1706','2015-11-30 13:18:20'),(44,'ticket','0035_usuarios_version','2015-11-30 13:18:21');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoreo_caracteristica`
--

DROP TABLE IF EXISTS `monitoreo_caracteristica`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoreo_caracteristica` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoreo_caracteristica`
--

LOCK TABLES `monitoreo_caracteristica` WRITE;
/*!40000 ALTER TABLE `monitoreo_caracteristica` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoreo_caracteristica` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoreo_equipos`
--

DROP TABLE IF EXISTS `monitoreo_equipos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoreo_equipos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  `name` varchar(120) NOT NULL,
  `descripcion` varchar(120) NOT NULL,
  `ubicacion` varchar(120) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  `ip` varchar(120) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `monitoreo_equipos_e8f8b1ef` (`empresa_id`),
  CONSTRAINT `monitoreo_equip_empresa_id_5bb95e841d701b8c_fk_ticket_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `ticket_empresa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoreo_equipos`
--

LOCK TABLES `monitoreo_equipos` WRITE;
/*!40000 ALTER TABLE `monitoreo_equipos` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoreo_equipos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoreo_parametro`
--

DROP TABLE IF EXISTS `monitoreo_parametro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoreo_parametro` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(120) NOT NULL,
  `puerto_origen` varchar(120) NOT NULL,
  `puerto_final` varchar(120) NOT NULL,
  `tipo` varchar(120) NOT NULL,
  `servicio` varchar(120) NOT NULL,
  `user` varchar(120) NOT NULL,
  `password` varchar(120) NOT NULL,
  `equipo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `monitoreo_parametro_f24bdbf2` (`equipo_id`),
  CONSTRAINT `monitoreo_par_equipo_id_45022b46b6063556_fk_monitoreo_equipos_id` FOREIGN KEY (`equipo_id`) REFERENCES `monitoreo_equipos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoreo_parametro`
--

LOCK TABLES `monitoreo_parametro` WRITE;
/*!40000 ALTER TABLE `monitoreo_parametro` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoreo_parametro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoreo_rango`
--

DROP TABLE IF EXISTS `monitoreo_rango`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoreo_rango` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `red_id` int(11) DEFAULT NULL,
  `tipo_id` int(11) DEFAULT NULL,
  `caracteristica_id` int(11) DEFAULT NULL,
  `ip` varchar(120) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `monitoreo_rango_e8f8b1ef` (`empresa_id`),
  KEY `monitoreo_rango_caracteristica_id_44b05a4608e60869_uniq` (`caracteristica_id`),
  KEY `monitoreo_rango_tipo_id_ffde5ec23826d01_uniq` (`tipo_id`),
  KEY `monitoreo_rango_red_id_5cceaf1455b0aea3_uniq` (`red_id`),
  CONSTRAINT `monitoreo_rango_empresa_id_5b1fbe7cceb056bf_fk_ticket_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `ticket_empresa` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoreo_rango`
--

LOCK TABLES `monitoreo_rango` WRITE;
/*!40000 ALTER TABLE `monitoreo_rango` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoreo_rango` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoreo_red`
--

DROP TABLE IF EXISTS `monitoreo_red`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoreo_red` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoreo_red`
--

LOCK TABLES `monitoreo_red` WRITE;
/*!40000 ALTER TABLE `monitoreo_red` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoreo_red` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monitoreo_tipo`
--

DROP TABLE IF EXISTS `monitoreo_tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `monitoreo_tipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(120) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monitoreo_tipo`
--

LOCK TABLES `monitoreo_tipo` WRITE;
/*!40000 ALTER TABLE `monitoreo_tipo` DISABLE KEYS */;
/*!40000 ALTER TABLE `monitoreo_tipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_archivo`
--

DROP TABLE IF EXISTS `ticket_archivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_archivo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `docfile` varchar(100) NOT NULL,
  `asunto` varchar(100) NOT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `ticket_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_archivo_649b92cd` (`ticket_id`),
  KEY `ticket_archivo_e8701ad4` (`user_id`),
  CONSTRAINT `ticket_archivo_ticket_id_5e8dbd20504803ed_fk_ticket_ticket_id` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_ticket` (`id`),
  CONSTRAINT `ticket_archivo_user_id_3b67f15928c744e0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_archivo`
--

LOCK TABLES `ticket_archivo` WRITE;
/*!40000 ALTER TABLE `ticket_archivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_archivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_chat`
--

DROP TABLE IF EXISTS `ticket_chat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_chat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `chat` varchar(100) DEFAULT NULL,
  `fecha` datetime DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_chat_e8701ad4` (`user_id`),
  CONSTRAINT `ticket_chat_user_id_120f959a211a1119_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_chat`
--

LOCK TABLES `ticket_chat` WRITE;
/*!40000 ALTER TABLE `ticket_chat` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_chat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_document`
--

DROP TABLE IF EXISTS `ticket_document`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_document` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `docfile` varchar(100) NOT NULL,
  `detalle` varchar(100) NOT NULL,
  `asunto` varchar(100) NOT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `ticket_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `asunto1` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_document_649b92cd` (`ticket_id`),
  KEY `ticket_document_e8701ad4` (`user_id`),
  CONSTRAINT `ticket_document_ticket_id_180cf9c13f97eb53_fk_ticket_ticket_id` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_ticket` (`id`),
  CONSTRAINT `ticket_document_user_id_27e65c60329f1820_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_document`
--

LOCK TABLES `ticket_document` WRITE;
/*!40000 ALTER TABLE `ticket_document` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_document` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_document_event`
--

DROP TABLE IF EXISTS `ticket_document_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_document_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `docfile` varchar(100) NOT NULL,
  `asunto` varchar(100) NOT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `evento_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_document_event_afb29da0` (`evento_id`),
  KEY `ticket_document_event_e8701ad4` (`user_id`),
  CONSTRAINT `ticket_document_event_user_id_27c6db1959f11ac7_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ticket_document_e_evento_id_5af1ab35c8582beb_fk_ticket_evento_id` FOREIGN KEY (`evento_id`) REFERENCES `ticket_evento` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_document_event`
--

LOCK TABLES `ticket_document_event` WRITE;
/*!40000 ALTER TABLE `ticket_document_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_document_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_empresa`
--

DROP TABLE IF EXISTS `ticket_empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_empresa` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(128) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_empresa`
--

LOCK TABLES `ticket_empresa` WRITE;
/*!40000 ALTER TABLE `ticket_empresa` DISABLE KEYS */;
INSERT INTO `ticket_empresa` VALUES (1,'Mego'),(2,'Xiencias'),(3,'Arzobispado de Lima'),(4,'Peru Veloz'),(5,'Xiencias-Adm');
/*!40000 ALTER TABLE `ticket_empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_estado`
--

DROP TABLE IF EXISTS `ticket_estado`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_estado` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `comentario` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_estado`
--

LOCK TABLES `ticket_estado` WRITE;
/*!40000 ALTER TABLE `ticket_estado` DISABLE KEYS */;
INSERT INTO `ticket_estado` VALUES (1,'Nuevo',NULL,''),(2,'Atendido',NULL,''),(3,'Prueba',NULL,''),(4,'Cerrado',NULL,''),(5,'Asignado',NULL,''),(6,'Reasignado',NULL,'');
/*!40000 ALTER TABLE `ticket_estado` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_evento`
--

DROP TABLE IF EXISTS `ticket_evento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_evento` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` longtext,
  `fecha_inicio` datetime DEFAULT NULL,
  `comentario` varchar(100) NOT NULL,
  `evento_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_evento_afb29da0` (`evento_id`),
  KEY `ticket_evento_e8701ad4` (`user_id`),
  CONSTRAINT `ticket_evento_evento_id_26370424846b3b0a_fk_ticket_ticket_id` FOREIGN KEY (`evento_id`) REFERENCES `ticket_ticket` (`id`),
  CONSTRAINT `ticket_evento_user_id_254eddd2b0b09fea_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_evento`
--

LOCK TABLES `ticket_evento` WRITE;
/*!40000 ALTER TABLE `ticket_evento` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_evento` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_notificaciones`
--

DROP TABLE IF EXISTS `ticket_notificaciones`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_notificaciones` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tipo` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `comentario` varchar(100) NOT NULL,
  `ticket_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_notificaciones_649b92cd` (`ticket_id`),
  CONSTRAINT `ticket_notificaci_ticket_id_510d2fed62c93c4a_fk_ticket_ticket_id` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_ticket` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_notificaciones`
--

LOCK TABLES `ticket_notificaciones` WRITE;
/*!40000 ALTER TABLE `ticket_notificaciones` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_notificaciones` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_soporte`
--

DROP TABLE IF EXISTS `ticket_soporte`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_soporte` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `titulo` varchar(1000) DEFAULT NULL,
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `comentario` varchar(100) NOT NULL,
  `soporte_id` int(11) NOT NULL,
  `ticket_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_soporte_3fdbe9ac` (`soporte_id`),
  KEY `ticket_soporte_649b92cd` (`ticket_id`),
  CONSTRAINT `ticket_soporte_soporte_id_274504348fbe370e_fk_auth_user_id` FOREIGN KEY (`soporte_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ticket_soporte_ticket_id_799030142baee935_fk_ticket_ticket_id` FOREIGN KEY (`ticket_id`) REFERENCES `ticket_ticket` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_soporte`
--

LOCK TABLES `ticket_soporte` WRITE;
/*!40000 ALTER TABLE `ticket_soporte` DISABLE KEYS */;
INSERT INTO `ticket_soporte` VALUES (1,'','2015-11-30 13:58:30','2015-11-30 14:01:08','',1,3),(2,'Hello','2015-11-30 14:04:36','2015-11-30 14:14:52','',6,3),(3,'','2015-11-30 14:02:22','2015-11-30 14:02:49','',1,2),(4,'','2015-11-30 14:02:33','2015-11-30 14:02:58','',1,1),(5,'Ded','2015-11-30 14:02:49',NULL,'',6,2),(6,'Cccc','2015-11-30 14:02:58',NULL,'',6,1),(7,'','2015-11-30 14:08:02',NULL,'',1,4),(8,'yuyu','2015-11-30 14:14:52',NULL,'',6,3),(9,'','2015-11-30 14:58:46',NULL,'',1,5),(10,'','2015-11-30 15:17:29',NULL,'',6,6),(11,'','2015-11-30 15:26:31',NULL,'',8,7),(12,'','2015-11-30 15:26:26',NULL,'',8,7),(13,'','2015-11-30 16:00:13',NULL,'',8,8);
/*!40000 ALTER TABLE `ticket_soporte` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_telefono`
--

DROP TABLE IF EXISTS `ticket_telefono`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_telefono` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `telefono` varchar(1000) NOT NULL,
  `tipo` varchar(1000) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_telefono_e8701ad4` (`user_id`),
  CONSTRAINT `ticket_telefono_user_id_245580f61d213731_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_telefono`
--

LOCK TABLES `ticket_telefono` WRITE;
/*!40000 ALTER TABLE `ticket_telefono` DISABLE KEYS */;
/*!40000 ALTER TABLE `ticket_telefono` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_ticket`
--

DROP TABLE IF EXISTS `ticket_ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_ticket` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `asunto` varchar(100) NOT NULL,
  `descripcion` longtext,
  `fecha_inicio` datetime NOT NULL,
  `fecha_fin` datetime DEFAULT NULL,
  `comentario` varchar(100) NOT NULL,
  `cliente_id` int(11) NOT NULL,
  `estado_id` int(11) NOT NULL,
  `tipo_id` int(11) NOT NULL,
  `soporte_actual` varchar(100) NOT NULL,
  `cancha` varchar(100) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ticket_ticket_4a860110` (`cliente_id`),
  KEY `ticket_ticket_2c189993` (`estado_id`),
  KEY `ticket_ticket_d3c0c18a` (`tipo_id`),
  KEY `ticket_ticket_e8f8b1ef` (`empresa_id`),
  CONSTRAINT `ticket_ticket_cliente_id_32b849e01179696b_fk_auth_user_id` FOREIGN KEY (`cliente_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `ticket_ticket_empresa_id_5be14b26ea97d13a_fk_ticket_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `ticket_empresa` (`id`),
  CONSTRAINT `ticket_ticket_estado_id_8d9b1f075d12928_fk_ticket_estado_id` FOREIGN KEY (`estado_id`) REFERENCES `ticket_estado` (`id`),
  CONSTRAINT `ticket_ticket_tipo_id_6590388084937106_fk_ticket_tipo_id` FOREIGN KEY (`tipo_id`) REFERENCES `ticket_tipo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_ticket`
--

LOCK TABLES `ticket_ticket` WRITE;
/*!40000 ALTER TABLE `ticket_ticket` DISABLE KEYS */;
INSERT INTO `ticket_ticket` VALUES (1,'Prueba','Hola','2015-11-30 13:34:10',NULL,'',1,6,1,'alvaro','Soporte',2),(2,'Prueba','Nooooo','2015-11-30 13:52:54',NULL,'',1,6,1,'alvaro','Soporte',2),(3,'Hola','Hello','2015-11-30 13:58:18',NULL,'',1,6,1,'alvaro','Soporte',2),(4,'hghg','ghgh','2015-11-30 14:04:46',NULL,'',1,2,1,'root','neutro',2),(5,'gfgfg','fgf','2015-11-30 14:15:02',NULL,'',1,5,1,'root','Soporte',2),(6,'P','p','2015-11-30 15:17:25',NULL,'',1,5,1,'alvaro','Soporte',2),(7,'hello','P','2015-11-30 15:23:56',NULL,'',1,5,1,'joel','Soporte',2),(8,'Please','holaaa','2015-11-30 15:59:36',NULL,'',3,5,1,'joel','Soporte',2);
/*!40000 ALTER TABLE `ticket_ticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_tipo`
--

DROP TABLE IF EXISTS `ticket_tipo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_tipo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `fecha_inicio` datetime DEFAULT NULL,
  `comentario` varchar(100) NOT NULL,
  `comentario1` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_tipo`
--

LOCK TABLES `ticket_tipo` WRITE;
/*!40000 ALTER TABLE `ticket_tipo` DISABLE KEYS */;
INSERT INTO `ticket_tipo` VALUES (1,'Incidencia',NULL,'',''),(2,'Requerimientos',NULL,'',''),(3,'Implementacion',NULL,'','');
/*!40000 ALTER TABLE `ticket_tipo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket_usuarios`
--

DROP TABLE IF EXISTS `ticket_usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ticket_usuarios` (
  `user_ptr_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL AUTO_INCREMENT,
  `direccion` varchar(100) NOT NULL,
  `ciudad` varchar(100) NOT NULL,
  `empresa_id` int(11) NOT NULL,
  `version` varchar(100) NOT NULL,
  PRIMARY KEY (`usuario_id`),
  UNIQUE KEY `user_ptr_id` (`user_ptr_id`),
  KEY `ticket_usuarios_e8f8b1ef` (`empresa_id`),
  CONSTRAINT `ticket_usuarios_empresa_id_109d10dddfe08583_fk_ticket_empresa_id` FOREIGN KEY (`empresa_id`) REFERENCES `ticket_empresa` (`id`),
  CONSTRAINT `ticket_usuarios_user_ptr_id_185452cd42c7b8a7_fk_auth_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket_usuarios`
--

LOCK TABLES `ticket_usuarios` WRITE;
/*!40000 ALTER TABLE `ticket_usuarios` DISABLE KEYS */;
INSERT INTO `ticket_usuarios` VALUES (1,3,'','',2,''),(2,4,'','',1,''),(3,5,'','',1,''),(4,6,'','',4,''),(5,7,'','',2,''),(6,8,'','',2,''),(7,9,'','',2,''),(8,10,'','',2,''),(9,11,'','',5,'');
/*!40000 ALTER TABLE `ticket_usuarios` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-11-30 16:16:21
