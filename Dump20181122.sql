CREATE DATABASE  IF NOT EXISTS `dmd` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `dmd`;
-- MySQL dump 10.13  Distrib 8.0.13, for Win64 (x86_64)
--
-- Host: localhost    Database: dmd
-- ------------------------------------------------------
-- Server version	8.0.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `car` (
  `CID` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Location` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `ChargeLevel` int(11) DEFAULT NULL,
  `Plug` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Color` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`CID`),
  UNIQUE KEY `CID_UNIQUE` (`CID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES ('AB012','78x87x22','Car',50,'A2','Blue'),('AN000','00x11x22','Rover',75,'A1','Red'),('BV022','0x0x0','Car',20,'A1','Green');
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `carparts`
--

DROP TABLE IF EXISTS `carparts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `carparts` (
  `CID` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `IsBroken` int(1) DEFAULT NULL,
  PRIMARY KEY (`CID`,`Type`),
  KEY `CID_idx` (`CID`),
  CONSTRAINT `CID` FOREIGN KEY (`CID`) REFERENCES `car` (`cid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `carparts`
--

LOCK TABLES `carparts` WRITE;
/*!40000 ALTER TABLE `carparts` DISABLE KEYS */;
INSERT INTO `carparts` VALUES ('AB012','bumper',0);
/*!40000 ALTER TABLE `carparts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chargingstation`
--

DROP TABLE IF EXISTS `chargingstation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `chargingstation` (
  `ChID` int(11) NOT NULL AUTO_INCREMENT,
  `zipcode` int(11) DEFAULT NULL,
  PRIMARY KEY (`ChID`),
  UNIQUE KEY `ChID_UNIQUE` (`ChID`),
  UNIQUE KEY `zipcode_UNIQUE` (`zipcode`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chargingstation`
--

LOCK TABLES `chargingstation` WRITE;
/*!40000 ALTER TABLE `chargingstation` DISABLE KEYS */;
INSERT INTO `chargingstation` VALUES (1,2),(2,3);
/*!40000 ALTER TABLE `chargingstation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `customer` (
  `username` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Email` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `PhoneNumber` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `CreditCard` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `zipcode` int(11) DEFAULT NULL,
  PRIMARY KEY (`username`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('asd','Asd','asd','908120909','123109283',4),('test111','Test','Subject','8800080','674833884',0);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `location` (
  `zipcode` int(11) NOT NULL AUTO_INCREMENT,
  `Address` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `City` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`zipcode`),
  UNIQUE KEY `zipcode_UNIQUE` (`zipcode`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Pushkina 177','Kazan'),(2,'Moskovsky, 188','Kazan'),(3,'Pushkinsky, 125','Kazan'),(4,'Lenina, 290','Kazan'),(5,'Putinskiy, 228','Kazan'),(6,'Velvet, 888','Kazan');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `payment` (
  `Date` date NOT NULL,
  `Cost` int(11) DEFAULT NULL,
  `username` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`Date`,`username`),
  KEY `username_idx` (`username`),
  KEY `username_payment_idx` (`username`),
  CONSTRAINT `username_payment` FOREIGN KEY (`username`) REFERENCES `customer` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `provider`
--

DROP TABLE IF EXISTS `provider`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `provider` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `zipcode` int(11) DEFAULT NULL,
  `name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phoneNumber` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`pid`),
  UNIQUE KEY `pid_UNIQUE` (`pid`),
  UNIQUE KEY `zipcode_UNIQUE` (`zipcode`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `provider`
--

LOCK TABLES `provider` WRITE;
/*!40000 ALTER TABLE `provider` DISABLE KEYS */;
INSERT INTO `provider` VALUES (1,5,'Shahid','88888888');
/*!40000 ALTER TABLE `provider` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `providerparts`
--

DROP TABLE IF EXISTS `providerparts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `providerparts` (
  `PID` int(11) NOT NULL,
  `Part` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Available` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Cost` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`PID`,`Part`),
  KEY `PID_idx` (`PID`),
  CONSTRAINT `PID` FOREIGN KEY (`PID`) REFERENCES `provider` (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `providerparts`
--

LOCK TABLES `providerparts` WRITE;
/*!40000 ALTER TABLE `providerparts` DISABLE KEYS */;
INSERT INTO `providerparts` VALUES (1,'bumper','300','200');
/*!40000 ALTER TABLE `providerparts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ride`
--

DROP TABLE IF EXISTS `ride`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `ride` (
  `username` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `CID` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `IsToCustomer` int(1) DEFAULT NULL,
  `BeginTime` time NOT NULL,
  `EndTime` time DEFAULT NULL,
  `Date` date NOT NULL,
  `OriginPoint` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `DestinationPoint` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Distance` int(11) DEFAULT NULL,
  `Cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`Date`,`BeginTime`,`CID`,`username`),
  KEY `CID_idx` (`CID`) /*!80000 INVISIBLE */,
  KEY `username_idx` (`username`),
  CONSTRAINT `car` FOREIGN KEY (`CID`) REFERENCES `car` (`cid`),
  CONSTRAINT `username` FOREIGN KEY (`username`) REFERENCES `customer` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ride`
--

LOCK TABLES `ride` WRITE;
/*!40000 ALTER TABLE `ride` DISABLE KEYS */;
INSERT INTO `ride` VALUES ('test111','AN000',0,'11:30:30','12:30:40','2018-09-22','00x00x00','24x25x26',10,300);
/*!40000 ALTER TABLE `ride` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sockets`
--

DROP TABLE IF EXISTS `sockets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `sockets` (
  `ChID` int(11) NOT NULL,
  `Type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Available` int(11) DEFAULT NULL,
  `TimeToCharge` int(11) DEFAULT NULL,
  `Cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`ChID`,`Type`),
  KEY `ChID_idx` (`ChID`),
  CONSTRAINT `ChID` FOREIGN KEY (`ChID`) REFERENCES `chargingstation` (`chid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sockets`
--

LOCK TABLES `sockets` WRITE;
/*!40000 ALTER TABLE `sockets` DISABLE KEYS */;
INSERT INTO `sockets` VALUES (1,'A1',6,30,200);
/*!40000 ALTER TABLE `sockets` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `socketslog`
--

DROP TABLE IF EXISTS `socketslog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `socketslog` (
  `CID` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `ChID` int(11) NOT NULL,
  `Type` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Date` date NOT NULL,
  `Time` time NOT NULL,
  PRIMARY KEY (`Time`,`Date`,`Type`),
  KEY `ChID,Type_idx` (`ChID`,`Type`),
  CONSTRAINT `ChID,Type` FOREIGN KEY (`ChID`, `Type`) REFERENCES `sockets` (`chid`, `type`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `socketslog`
--

LOCK TABLES `socketslog` WRITE;
/*!40000 ALTER TABLE `socketslog` DISABLE KEYS */;
INSERT INTO `socketslog` VALUES ('AN012',1,'A1','2020-01-15','22:00:00');
/*!40000 ALTER TABLE `socketslog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `workshop`
--

DROP TABLE IF EXISTS `workshop`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `workshop` (
  `WID` int(11) NOT NULL AUTO_INCREMENT,
  `zipcode` int(11) DEFAULT NULL,
  PRIMARY KEY (`WID`),
  UNIQUE KEY `WID_UNIQUE` (`WID`),
  UNIQUE KEY `zipcode_UNIQUE` (`zipcode`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `workshop`
--

LOCK TABLES `workshop` WRITE;
/*!40000 ALTER TABLE `workshop` DISABLE KEYS */;
INSERT INTO `workshop` VALUES (2,5),(1,6);
/*!40000 ALTER TABLE `workshop` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wparts`
--

DROP TABLE IF EXISTS `wparts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `wparts` (
  `WID` int(11) NOT NULL,
  `Part` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Available` int(11) DEFAULT NULL,
  `Cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`WID`,`Part`),
  CONSTRAINT `WID` FOREIGN KEY (`WID`) REFERENCES `workshop` (`wid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wparts`
--

LOCK TABLES `wparts` WRITE;
/*!40000 ALTER TABLE `wparts` DISABLE KEYS */;
INSERT INTO `wparts` VALUES (1,'bumper',6,300),(2,'bumper',3,250);
/*!40000 ALTER TABLE `wparts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wshoplog`
--

DROP TABLE IF EXISTS `wshoplog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `wshoplog` (
  `WID` int(11) NOT NULL,
  `CID` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `Part` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `Date` date DEFAULT NULL,
  `Cost` int(11) DEFAULT NULL,
  PRIMARY KEY (`WID`,`Part`),
  CONSTRAINT `WID,Part` FOREIGN KEY (`WID`, `Part`) REFERENCES `wparts` (`wid`, `part`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wshoplog`
--

LOCK TABLES `wshoplog` WRITE;
/*!40000 ALTER TABLE `wshoplog` DISABLE KEYS */;
INSERT INTO `wshoplog` VALUES (1,'AB012','bumper','2022-01-12',300);
/*!40000 ALTER TABLE `wshoplog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-22 13:43:14