-- MySQL dump 10.13  Distrib 8.3.0, for macos13.6 (arm64)
--
-- Host: localhost    Database: gsg
-- ------------------------------------------------------
-- Server version	8.3.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('9a94f99adc25');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `message`
--

DROP TABLE IF EXISTS `message`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `message` (
  `id` int NOT NULL AUTO_INCREMENT,
  `sender_id` int NOT NULL,
  `recipient_id` int NOT NULL,
  `content` text NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `read` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sender_id` (`sender_id`),
  KEY `recipient_id` (`recipient_id`),
  KEY `ix_message_timestamp` (`timestamp`),
  CONSTRAINT `message_ibfk_1` FOREIGN KEY (`sender_id`) REFERENCES `user` (`id`),
  CONSTRAINT `message_ibfk_2` FOREIGN KEY (`recipient_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `message`
--

LOCK TABLES `message` WRITE;
/*!40000 ALTER TABLE `message` DISABLE KEYS */;
INSERT INTO `message` VALUES (1,3,1,'hello how are you','2024-03-04 23:52:14',0),(2,1,3,'good and how are you?','2024-03-04 23:52:40',0),(3,3,1,'very well thank you ','2024-03-04 23:53:06',0),(4,1,3,'test','2024-03-04 23:53:55',0),(5,3,1,'testing','2024-03-04 23:54:12',0),(6,4,1,'hello is the property at 8 surrey lane available?','2024-03-05 05:32:25',0),(7,1,4,'Yes','2024-03-05 05:32:44',0),(8,5,1,'hello is the apartment at 7 tulane dr pet friendly?','2024-03-05 13:52:29',0),(9,1,5,'yes the apartment is pet friendly so long as you clean up after the animal','2024-03-05 13:53:05',0),(10,6,1,'hello is the property available\n','2024-03-05 15:41:44',0),(11,1,6,'yes it is ','2024-03-05 15:42:22',0),(12,1,4,'yo','2024-03-20 21:46:35',0),(13,7,1,'helloo \n','2024-03-21 20:43:16',0),(14,7,1,'how are you','2024-03-21 20:43:22',0),(15,8,1,'Hey owner','2024-03-25 17:58:33',0),(16,4,1,'hello ','2024-03-26 18:09:42',0),(17,4,1,'how\n','2024-03-26 18:09:49',0),(18,4,1,'are','2024-03-26 18:09:51',0),(19,4,1,'you','2024-03-26 18:09:54',0),(20,4,1,'h','2024-03-26 18:09:57',0),(21,4,1,'h','2024-03-26 18:10:00',0),(22,4,1,'h','2024-03-26 18:10:02',0),(23,4,1,'h','2024-03-26 18:10:04',0),(24,4,1,'h','2024-03-26 18:10:05',0),(25,4,1,'h','2024-03-26 18:10:07',0),(26,1,4,'h','2024-03-26 18:11:33',0),(27,1,4,'hi ','2024-03-26 18:11:36',0),(28,1,4,'ewf','2024-03-26 18:11:58',0),(29,1,4,'wefewf','2024-03-26 18:12:00',0),(30,1,4,'wefew','2024-03-26 18:12:01',0),(31,1,4,'ewfwe','2024-03-26 18:12:01',0),(32,1,4,'fwe','2024-03-26 18:12:02',0),(33,1,4,'fwe','2024-03-26 18:12:02',0),(34,1,4,'f','2024-03-26 18:12:02',0),(35,1,4,'we','2024-03-26 18:12:02',0),(36,1,4,'we','2024-03-26 18:12:03',0),(37,1,4,'f','2024-03-26 18:12:03',0),(38,1,4,'f','2024-03-26 18:12:03',0),(39,1,4,'f','2024-03-26 18:12:03',0),(40,1,4,'we','2024-03-26 18:12:03',0),(41,1,4,'we','2024-03-26 18:12:04',0),(42,1,4,'fwefwe','2024-03-26 18:12:17',0),(43,1,5,'hola','2024-03-27 20:45:50',0),(44,9,1,'Hi. Im excited to stay at Cozy House.\n','2024-03-28 00:55:10',0),(45,1,9,'Ook cool','2024-03-28 00:56:43',0),(46,10,1,'hello \n','2024-03-28 14:14:58',0),(47,1,10,'hi','2024-03-28 14:26:55',0),(48,4,1,'hi\n','2024-04-02 01:25:07',0),(49,4,1,'hello','2024-04-02 12:58:09',0),(50,3,1,'hello\n','2024-04-02 14:37:46',0),(51,1,3,'hi','2024-04-02 14:39:12',0),(52,1,3,'hi','2024-04-02 14:39:17',0);
/*!40000 ALTER TABLE `message` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `photos`
--

DROP TABLE IF EXISTS `photos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` varchar(255) NOT NULL,
  `property_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_id` (`property_id`),
  CONSTRAINT `photos_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `property_listing` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `photos`
--

LOCK TABLES `photos` WRITE;
/*!40000 ALTER TABLE `photos` DISABLE KEYS */;
INSERT INTO `photos` VALUES (4,'a5ce0bfe0e26e1f626ef0b08af738226-full.jpg',11),(5,'c7b17f7785a50c34b70526cd86f1f703-cc_ft_1344.jpg',12),(6,'b450a2fbf4da22f4a5df89deefd5c16b-cc_ft_768.jpg',13),(7,'3f47e55f7e994d139de7ca7db637066ed14a185d-1-medium.jpeg',14),(9,'3f47e55f7e994d139de7ca7db637066ed14a185d-1-medium.jpeg',16);
/*!40000 ALTER TABLE `photos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `property_listing`
--

DROP TABLE IF EXISTS `property_listing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `property_listing` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(100) NOT NULL,
  `description` text NOT NULL,
  `price` int NOT NULL,
  `location` varchar(100) NOT NULL,
  `timestamp` datetime DEFAULT NULL,
  `bedrooms` int NOT NULL,
  `bathrooms` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_property_listing_timestamp` (`timestamp`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `property_listing`
--

LOCK TABLES `property_listing` WRITE;
/*!40000 ALTER TABLE `property_listing` DISABLE KEYS */;
INSERT INTO `property_listing` VALUES (11,'Cozy House ','Nestled in the heart of Atlantic City, this charming abode offers the perfect blend of comfort and convenience. Boasting three bedrooms and three bathrooms, this cozy house is ideal for families or small groups seeking a tranquil retreat by the Atlantic coast. Step inside to discover a warm and inviting atmosphere, with tasteful decor and ample natural light creating an ambiance of relaxation.',800,'93 E Rutherford dr, Atlantic City ','2024-03-27 22:48:40',3,3),(12,'Spacious Cottage ','Welcome to your luxurious beachfront retreat in Atlantic City! This stunning 5-bedroom, 5-bathroom house offers breathtaking views of the ocean from every angle. Relax and rejuvenate in the private Jacuzzi while soaking in the serene sounds of the waves crashing nearby. With spacious living areas and stylish decor throughout, this exquisite home provides the ultimate coastal getaway for you and your guests.',1400,'37 Boston dr, Atlantic City ','2024-03-27 22:54:30',5,5),(13,'Shoreline Serenity','\"Shoreline Serenity\" offers a tranquil escape in Atlantic City, featuring 3 bedrooms and 4 bathrooms. Enjoy stunning coastal views from this stylish retreat, where comfort meets luxury. With spacious living areas and a gourmet kitchen, it\'s the perfect place to unwind. Relax on the private terrace or explore the vibrant seaside scene nearby.',2000,'1616 Pacific Ave, Atlantic City ','2024-03-27 23:22:04',3,4),(14,'Big Nice House','Big',1000,'123 My Crib Rd','2024-03-28 00:59:50',4,6),(16,'BeachHouse','fits 12 people',500,'123 Beach St','2024-04-02 14:40:17',5,4);
/*!40000 ALTER TABLE `property_listing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reservation` (
  `id` int NOT NULL AUTO_INCREMENT,
  `property_id` int NOT NULL,
  `user_id` int NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL,
  `status` varchar(100) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `property_id` (`property_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reservation_ibfk_1` FOREIGN KEY (`property_id`) REFERENCES `property_listing` (`id`),
  CONSTRAINT `reservation_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (1,12,4,'2024-03-28 00:00:00','2024-04-05 00:00:00','pending',12600.00),(2,11,9,'2024-08-01 00:00:00','2024-08-04 00:00:00','pending',3200.00),(3,11,10,'2024-03-30 00:00:00','2024-03-31 00:00:00','pending',1600.00),(4,12,3,'2024-03-29 00:00:00','2024-04-01 00:00:00','pending',5600.00),(5,12,1,'2024-04-04 00:00:00','2024-04-05 00:00:00','pending',2800.00),(6,14,3,'2024-04-03 00:00:00','2024-04-11 00:00:00','pending',9000.00),(7,11,3,'2024-04-03 00:00:00','2024-04-10 00:00:00','pending',6400.00);
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password_hash` varchar(255) NOT NULL,
  `is_admin` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Jorge','Jorgegonzales191421@gmail.com','scrypt:32768:8:1$TkOkqp1NIulLFjDh$c2e642f3a4b2fe1fae61c14bc3897cff380b4d6f8994bf2a2612855091e5dcc067805bfe37936e5a060ba0074f315399b56ed38a9001b767ed5e13e26fd33382',1),(3,'Luke','luke@gmail.com','scrypt:32768:8:1$dxvPNgl59vOlhgaX$80c013ba3f8b267fa865c20a8238190fcdde7adb6aab20dafe50ff7c2f0c9716e7ba0f3bdc9fb3a26c65f83f8c17ac822417e2bbe8d67c6551457d5c7e512cc2',0),(4,'Thomas','Thomas@Gmail.com','scrypt:32768:8:1$y5iBgePvxczNpQWR$687e1129c37f60b68307ead469f6f6b14ed39a76b5f1d1818fc52b268941f9d790c69a725cf8846b810b5059de519efea435be1c09cd3e7a797d4d35ae972545',0),(5,'Jack ','jack@gmail.com','scrypt:32768:8:1$UkJkETXKabcisH6C$7dfa6e6ed12ea870fd19ae1dae40496c9eeae4bd5dc50f396b295b9e57666182726f8a4b5aaefec4af992c2e3e2f4ecafd7fbc3f680a836c2689b0d1311dd21f',0),(6,'Cody','c@gmail.com','scrypt:32768:8:1$20bPN8MrQ6VCcxzr$93fe3261ebbcf762fa212bd756451f58617e71ef79a4d879ef724adcb5efb28b36ef4e76879f403f4cf3fe9aa7ea5806d3620a98ca618d731a3315417660c17b',0),(7,'pablo','pablo@gmail.com','scrypt:32768:8:1$EHQbRL0FzCb5wsC2$b3a5ec65ce38b6051241a9728f62ab5b51da265311b4d186cb4c7ed36ef65388e8ac10d7052e94d5800312b62cc027f0122b40c2f17fa57ffed0b14851d6637a',0),(8,'diego','deigo@gmail.com','scrypt:32768:8:1$ZJmm8PbmX2vYi995$7a6c3ef473305b57042239e5c34d96269d6c620cddd450664743a8f64547b258d6a7712b6343ee52bf0289f81be91d9477d7e1b19bdfbf5e7f224dea0c1f2816',0),(9,'timmy','timmy@gmail.com','scrypt:32768:8:1$vAixyir0HZd2jWRd$eee3beb6516ebe9974506574b19f3a397d98c5918a79eb7828f2deac4740249751f08ef32733b1b6190ad13457ffa0906a0b070e561005d74fa6cf9c91f3604a',0),(10,'dan','dan@gmail.com','scrypt:32768:8:1$e6K90QFIYseLate2$57294fa05b3bd496fb440509d4f4f31151c255a5d354627547e357de29f94778a2bd4c735350b1318c38f2d4b1b51ca5346da3f900950a3590517241d1b712cf',0),(11,'tester','tester@gmail.com','scrypt:32768:8:1$dpaaxWNPIwfPkovo$7b7d464f9397d2bee3c62a652183faed0618717c7c2653b4ce2169d6a675bae8c9d3deb793e5722dc81642c32fc222d47eecf81f4d21e58863c2c75e8dae420d',0),(12,'Dylan','dyan@gmail.com','scrypt:32768:8:1$dyYfqojgJooe4fmv$cb4dc785e1c3fe438e6417749e024efb288c2d390deb2ffaca0d691d900e36c3758f30f18c79a6b015f5f8a621a4842a9bc5cb2aad021c50c45d8cab9a4b1f6d',0);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-02 11:11:52
