-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: itbooks
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `baocaocongno`
--

DROP TABLE IF EXISTS `baocaocongno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baocaocongno` (
  `id` int NOT NULL AUTO_INCREMENT,
  `thang` date NOT NULL,
  `noDau` decimal(10,0) NOT NULL,
  `phatSinh` decimal(10,0) NOT NULL,
  `khachHang_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `khachHang_id` (`khachHang_id`),
  CONSTRAINT `baocaocongno_ibfk_1` FOREIGN KEY (`khachHang_id`) REFERENCES `khachhang` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baocaocongno`
--

LOCK TABLES `baocaocongno` WRITE;
/*!40000 ALTER TABLE `baocaocongno` DISABLE KEYS */;
/*!40000 ALTER TABLE `baocaocongno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `baocaoton`
--

DROP TABLE IF EXISTS `baocaoton`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `baocaoton` (
  `id` int NOT NULL AUTO_INCREMENT,
  `tonDau` decimal(10,0) NOT NULL,
  `phatSinh` decimal(10,0) NOT NULL,
  `tonCuoi` decimal(10,0) NOT NULL,
  `ms` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ms` (`ms`),
  CONSTRAINT `baocaoton_ibfk_1` FOREIGN KEY (`ms`) REFERENCES `sach` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `baocaoton`
--

LOCK TABLES `baocaoton` WRITE;
/*!40000 ALTER TABLE `baocaoton` DISABLE KEYS */;
/*!40000 ALTER TABLE `baocaoton` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitiethoadon`
--

DROP TABLE IF EXISTS `chitiethoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitiethoadon` (
  `soLuong` int NOT NULL,
  `donGia` decimal(10,0) NOT NULL,
  `thanhTien` decimal(10,0) NOT NULL,
  `hoaDon_id` int NOT NULL,
  `sach_id` int NOT NULL,
  PRIMARY KEY (`hoaDon_id`,`sach_id`),
  KEY `sach_id` (`sach_id`),
  CONSTRAINT `chitiethoadon_ibfk_1` FOREIGN KEY (`hoaDon_id`) REFERENCES `hoadon` (`id`),
  CONSTRAINT `chitiethoadon_ibfk_2` FOREIGN KEY (`sach_id`) REFERENCES `sach` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitiethoadon`
--

LOCK TABLES `chitiethoadon` WRITE;
/*!40000 ALTER TABLE `chitiethoadon` DISABLE KEYS */;
/*!40000 ALTER TABLE `chitiethoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `chitietphieunhap`
--

DROP TABLE IF EXISTS `chitietphieunhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `chitietphieunhap` (
  `soLuong` int NOT NULL,
  `phieuNhap_id` int NOT NULL,
  `sach_id` int NOT NULL,
  PRIMARY KEY (`phieuNhap_id`,`sach_id`),
  KEY `sach_id` (`sach_id`),
  CONSTRAINT `chitietphieunhap_ibfk_1` FOREIGN KEY (`phieuNhap_id`) REFERENCES `phieunhap` (`id`),
  CONSTRAINT `chitietphieunhap_ibfk_2` FOREIGN KEY (`sach_id`) REFERENCES `sach` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `chitietphieunhap`
--

LOCK TABLES `chitietphieunhap` WRITE;
/*!40000 ALTER TABLE `chitietphieunhap` DISABLE KEYS */;
INSERT INTO `chitietphieunhap` VALUES (100,2,2),(200,3,1),(30,3,3);
/*!40000 ALTER TABLE `chitietphieunhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hoadon`
--

DROP TABLE IF EXISTS `hoadon`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `hoadon` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngayLapHD` date NOT NULL,
  `khachHang_id` int NOT NULL,
  `nhanVien_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `khachHang_id` (`khachHang_id`),
  KEY `nhanVien_id` (`nhanVien_id`),
  CONSTRAINT `hoadon_ibfk_1` FOREIGN KEY (`khachHang_id`) REFERENCES `khachhang` (`id`),
  CONSTRAINT `hoadon_ibfk_2` FOREIGN KEY (`nhanVien_id`) REFERENCES `nhanvien` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hoadon`
--

LOCK TABLES `hoadon` WRITE;
/*!40000 ALTER TABLE `hoadon` DISABLE KEYS */;
/*!40000 ALTER TABLE `hoadon` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `khachhang`
--

DROP TABLE IF EXISTS `khachhang`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `khachhang` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(55) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `diaChi` varchar(250) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `dienThoai` varchar(15) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `khachhang`
--

LOCK TABLES `khachhang` WRITE;
/*!40000 ALTER TABLE `khachhang` DISABLE KEYS */;
/*!40000 ALTER TABLE `khachhang` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `khachhangno`
--

DROP TABLE IF EXISTS `khachhangno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `khachhangno` (
  `ngayNo` date NOT NULL,
  `soTien` decimal(10,0) NOT NULL,
  `khachHang_id` int NOT NULL,
  PRIMARY KEY (`ngayNo`),
  KEY `khachHang_id` (`khachHang_id`),
  CONSTRAINT `khachhangno_ibfk_1` FOREIGN KEY (`khachHang_id`) REFERENCES `khachhang` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `khachhangno`
--

LOCK TABLES `khachhangno` WRITE;
/*!40000 ALTER TABLE `khachhangno` DISABLE KEYS */;
/*!40000 ALTER TABLE `khachhangno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nhanvien`
--

DROP TABLE IF EXISTS `nhanvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nhanvien` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(55) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `ngaySinh` date NOT NULL,
  `diaChi` varchar(100) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `cmnd` varchar(15) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nhanvien`
--

LOCK TABLES `nhanvien` WRITE;
/*!40000 ALTER TABLE `nhanvien` DISABLE KEYS */;
/*!40000 ALTER TABLE `nhanvien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieunhap`
--

DROP TABLE IF EXISTS `phieunhap`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieunhap` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngayNhap` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieunhap`
--

LOCK TABLES `phieunhap` WRITE;
/*!40000 ALTER TABLE `phieunhap` DISABLE KEYS */;
INSERT INTO `phieunhap` VALUES (1,'2020-11-29'),(2,'2020-12-17'),(3,'2020-12-31');
/*!40000 ALTER TABLE `phieunhap` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phieuthutienno`
--

DROP TABLE IF EXISTS `phieuthutienno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `phieuthutienno` (
  `id` int NOT NULL AUTO_INCREMENT,
  `ngayThu` date NOT NULL,
  `soTien` decimal(10,0) NOT NULL,
  `khachHang_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `khachHang_id` (`khachHang_id`),
  CONSTRAINT `phieuthutienno_ibfk_1` FOREIGN KEY (`khachHang_id`) REFERENCES `khachhang` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phieuthutienno`
--

LOCK TABLES `phieuthutienno` WRITE;
/*!40000 ALTER TABLE `phieuthutienno` DISABLE KEYS */;
/*!40000 ALTER TABLE `phieuthutienno` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sach`
--

DROP TABLE IF EXISTS `sach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sach` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(55) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `donGia` decimal(10,0) NOT NULL,
  `avatar` varchar(255) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `theLoai_id` int NOT NULL,
  `tacGia_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `theLoai_id` (`theLoai_id`),
  KEY `tacGia_id` (`tacGia_id`),
  CONSTRAINT `sach_ibfk_1` FOREIGN KEY (`theLoai_id`) REFERENCES `theloai` (`id`),
  CONSTRAINT `sach_ibfk_2` FOREIGN KEY (`tacGia_id`) REFERENCES `tacgia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sach`
--

LOCK TABLES `sach` WRITE;
/*!40000 ALTER TABLE `sach` DISABLE KEYS */;
INSERT INTO `sach` VALUES (1,'Mắt Biếc',90000,'images/avatar/mắt_biếc.jpeg','Chuyện kể về Ngạn ngok ngeck\'...',4,1),(2,'Thần Đồng Đất Việt - Pháp Sư Gọi Bưởi',15000,'images/avatar/datviet_tap1.jpg','Nhóm bạn Tý Sữu Dần Mẹo',5,2),(3,'Thần Đồng Đất Việt - Trí Nhớ Siêu Phàm',15000,'images/avatar/datviet_tap2.jpg','Nhóm bạn Tý Sữu Dần Mẹo',5,2),(4,'Thần Đồng Đất Việt - Voi Đất Biết Đi',15000,'images/avatar/datviet_tap3.png','Chuyện kể về Ngạn ngok ngeck\'...',5,2);
/*!40000 ALTER TABLE `sach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `soluongsach`
--

DROP TABLE IF EXISTS `soluongsach`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `soluongsach` (
  `sach_id` int NOT NULL,
  `soLuong` int NOT NULL,
  PRIMARY KEY (`sach_id`),
  CONSTRAINT `soluongsach_ibfk_1` FOREIGN KEY (`sach_id`) REFERENCES `sach` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `soluongsach`
--

LOCK TABLES `soluongsach` WRITE;
/*!40000 ALTER TABLE `soluongsach` DISABLE KEYS */;
/*!40000 ALTER TABLE `soluongsach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tacgia`
--

DROP TABLE IF EXISTS `tacgia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tacgia` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nametg` varchar(55) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tacgia`
--

LOCK TABLES `tacgia` WRITE;
/*!40000 ALTER TABLE `tacgia` DISABLE KEYS */;
INSERT INTO `tacgia` VALUES (1,'Nguyễn Nhật Ánh'),(2,'Lê Linh');
/*!40000 ALTER TABLE `tacgia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `theloai`
--

DROP TABLE IF EXISTS `theloai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `theloai` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nametl` varchar(55) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `theloai`
--

LOCK TABLES `theloai` WRITE;
/*!40000 ALTER TABLE `theloai` DISABLE KEYS */;
INSERT INTO `theloai` VALUES (1,'Kiếm Hiệp'),(2,'Hành Động'),(3,'Dân Gian'),(4,'Tình Cảm'),(5,'Thiếu Nhi');
/*!40000 ALTER TABLE `theloai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(55) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `email` varchar(50) COLLATE utf8mb4_vi_0900_as_cs DEFAULT NULL,
  `username` varchar(50) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `password` varchar(50) COLLATE utf8mb4_vi_0900_as_cs NOT NULL,
  `avatar` varchar(100) COLLATE utf8mb4_vi_0900_as_cs DEFAULT NULL,
  `active` tinyint(1) DEFAULT NULL,
  `user_role` enum('KH','USER','ADMIN') COLLATE utf8mb4_vi_0900_as_cs DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  CONSTRAINT `user_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vi_0900_as_cs;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'admin','admin@gmail','admin','e10adc3949ba59abbe56e057f20f883e',NULL,1,'ADMIN'),(2,'Thanh','thanh@gmail.com','thanhuser','e10adc3949ba59abbe56e057f20f883e','images/uploads/toan112.jpg',1,'KH');
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

-- Dump completed on 2020-12-09 21:35:51
