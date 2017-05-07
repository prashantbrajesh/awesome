-- MySQL dump 10.13  Distrib 5.7.10, for osx10.9 (x86_64)
--
-- Host: localhost    Database: urdb
-- ------------------------------------------------------
-- Server version	5.7.10

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
-- Table structure for table `BooksDocTarRarZipTxtTable`
--

DROP TABLE IF EXISTS `BooksDocTarRarZipTxtTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BooksDocTarRarZipTxtTable` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `Other*********fo` text,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `BooksPdfTable`
--

DROP TABLE IF EXISTS `BooksPdfTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `BooksPdfTable` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `Other*********fo` text,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `GamesApkTable`
--

DROP TABLE IF EXISTS `GamesApkTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GamesApkTable` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `Other*********fo` text,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `GamesJarJadTable`
--

DROP TABLE IF EXISTS `GamesJarJadTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `GamesJarJadTable` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `Other*********fo` text,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `SongsMp3Table`
--

DROP TABLE IF EXISTS `SongsMp3Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SongsMp3Table` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `UrlHealthTable`
--

DROP TABLE IF EXISTS `UrlHealthTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UrlHealthTable` (
  `TableName` varchar(50) CHARACTER SET utf8 NOT NULL,
  `UniqueID` big*********t(10) NOT NULL,
  `DownloadUrl` text,
  `HealthValue` big*********t(2) DEFAULT NULL,
  `LastCheckedTime` datetime DEFAULT NULL,
  `LastStatus` enum('0','1') DEFAULT NULL,
  UNIQUE KEY `UniqueIDWithTable` (`TableName`,`UniqueID`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Videos3gpTable`
--

DROP TABLE IF EXISTS `Videos3gpTable`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Videos3gpTable` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `VideosMp4Table`
--

DROP TABLE IF EXISTS `VideosMp4Table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `VideosMp4Table` (
  `UniqueId` big*********t(10) NOT NULL,
  `FileName` text,
  `DownloadUrl` text NOT NULL,
  `RefRedirectUrl` text,
  `FileSize` big*********t(4) DEFAULT NULL,
  `ImgThumbUrl` text,
  `*********sertTime` datetime DEFAULT NULL,
  `health` big*********t(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`UniqueId`),
  UNIQUE KEY `UniqueURL` (`DownloadUrl`(255)),
  FULLTEXT KEY `SearchFileName` (`FileName`)
) ENG*********E=MyISAM DEFAULT CHARSET=lat*********1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump *********pleted on 2016-07-17 22:23:59
