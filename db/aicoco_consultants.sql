-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: localhost    Database: aicoco
-- ------------------------------------------------------
-- Server version	5.7.19-log

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
-- Table structure for table `consultants`
--

DROP TABLE IF EXISTS `consultants`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consultants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `姓名` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `學歷` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `經歷` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `證照` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `image` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL,
  `操盤特色` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL,
  `url` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consultants`
--

LOCK TABLES `consultants` WRITE;
/*!40000 ALTER TABLE `consultants` DISABLE KEYS */;
INSERT INTO `consultants` VALUES (18,'宋智孝','留美MBA','富強投顧　證券分析師','理財規劃顧問師','宋智孝.jpg','「卓越的績效不是行為，只是習慣；成功的投資不在標得，而是意念。」「籌碼面」、「技術面」、「基本面」是多數的市場交易者所談論的「術」。而真的贏家和大師級的人物，卻是以「道」為出發。「有道無術，只能紙上談兵；有術無道，不能登峰造極。」量子操盤室將量子的概念附加於股市上，回歸原點，由點到面的選股邏輯，精確掌握。 將複雜的數據，化做簡單的獲利，帶領投資朋友邁向璀璨的人生！','https://www.youtube.com/watch?v=Ou4SYzxdwr8'),(19,'朴寶英','留美MBA','嘉德投顧　證券分析師','證券、期貨雙分析師','朴寶英.jpeg','簡單、量化股票漲，靠錢堆，漲升的過程中，多數是有共通邏輯的，量會如何？價會如何？K線表現如何？籌碼表現如何？透過量價籌碼的精算，找出當前正在多頭運動的股票，賺取最好賺的一段，減少時間成本及抱股風險。','https://www.youtube.com/watch?v=u-NeRIABZPM'),(20,'周子瑜','美國聖路易大學財金所碩士','新竹國際商銀','理財規劃顧問師','周子瑜.jpg','結合世界各國股神(美國巴菲特、索羅斯、彼得林區,德國科斯托蘭尼，日本是川銀藏。正確的觀念，配合紮實產業的分析能力，加上掌握第一手產業的資訊，切入未來明星飆股。讓會員以最少的資金，在最短的時間內，創造最大的獲利!','https://www.youtube.com/watch?v=z2PSIjKz0Jw'),(21,'李聖經','美國奧克拉荷馬州立中央大學','嘉德投顧　證券分析師 ','理財規劃顧問師','李聖經.jpg','30年股市多空實戰經驗 法人圈基本面研究與自營操盤 型態戰法，掌握關鍵轉折 飆股重壓，讓你獲利極大化！','https://www.youtube.com/watch?v=8qnbplBvuNc'),(22,'秀智','中興大學法商學院','第一證券　研究部協理','證券商高級營業員','秀智.jpg','重視國際趨勢，根據外匯，黃金，石油、、、等國際影響因素，分析大趨勢，再配合國內總體經濟指標切入產業分析，選擇質優的投資標的，研究其技術分析統計圖形，為您找出最佳時點買入及賣出，追求獲利極大值，控制風險能力敏銳，達成風險極小值的目的。','https://www.youtube.com/watch?v=yR5uO9Lwc9M'),(23,'Jiae','國立台北大學企業管理研究所碩士班畢業','鼎燁投顧　證券分析師','財富管理規劃師','Jiae.jpg','「戲法人人會變，各有巧妙不同」，市面上有關於投資理財的書千千百百種，為什麼許多投資人讀了這麼多還是賺不到錢?最大的癥結所在，還是沒有具體的『操盤的技巧』與『正確的情緒管理』。因此，投資朋友您一定要衡量自己的『能力』與『個性』，找到適合自己的投資方式，如此才能在股海裡生存。所以，您除了要學習控制自己的信念之外，還包含思想、情緒、感覺、需要、希望、目標、恐懼、害怕、憤怒、失望、耐心、壓力、焦慮等。想要在股市中成為贏家，不是那麼簡單的!我除了要讓您懂得所有影響股市的因素，包括「國際面」、「政策面」、「產業面」、「資金面」、「消息面」、「基本面」、「技術面」以及「籌碼面」的專業看法及操盤技巧之外，我還要培養您股市贏家的心理因子，讓您一輩子都受用。','https://www.youtube.com/watch?v=A-0jPNf25Xc'),(24,'solar','中興大學法商學院','大信綜合證券總公司營業櫃主管','理財規劃顧問師','solar.jpg','以基本面的總經數據、產業脈動為主軸，領先掌握大盤及個股趨勢，輔以技術面的多空動能系統、量價結構及型態分析尋找最佳買賣點，進而擬定妥善的操作策略及資金控管，賺取多空雙向波段利潤','https://www.youtube.com/watch?v=0gmZBW3Ngf0'),(25,'娜璉','國立台北大學企業管理研究所碩士班畢業','富強投顧　證券分析師','特許財務分析師','娜璉.jpeg','股市歷練二十餘載，尊重趨勢、波段操作、順勢而為。法人操盤經驗深厚，深刻了解法人操作模式，洞悉股市型態，全面考量各大類股輪動模式，精準掌握主流，穩健、安全地替投資人獲取最大的利潤。多空雙向的指數操作，精準的盤勢分析，獨到的看盤功力，果決的判斷，帶進帶出，是少數能將預測、分析、操作合而為一的分析師。','https://www.youtube.com/watch?v=WpA3NP-jqu4'),(26,'張上遠','留美MBA','玉峰投顧　證券分析師','證券商高級營業員 特許財務分析師','周潤發.jpg','「戲法人人會變，各有巧妙不同」，市面上有關於投資理財的書千千百百種，為什麼許多投資人讀了這麼多還是賺不到錢?最大的癥結所在，還是沒有具體的『操盤的技巧』與『正確的情緒管理』。因此，投資朋友您一定要衡量自己的『能力』與『個性』，找到適合自己的投資方式，如此才能在股海裡生存。所以，您除了要學習控制自己的信念之外，還包含思想、情緒、感覺、需要、希望、目標、恐懼、害怕、憤怒、失望、耐心、壓力、焦慮等。想要在股市中成為贏家，不是那麼簡單的!我除了要讓您懂得所有影響股市的因素，包括「國際面」、「政策面」、「產業面」、「資金面」、「消息面」、「基本面」、「技術面」以及「籌碼面」的專業看法及操盤技巧之外，我還要培養您股市贏家的心理因子，讓您一輩子都受用。',''),(27,'Richard','美國南加大USC','與股神巴菲特征戰股海30餘年','證券商高級營業員 特許財務分析師','member4.jpg','30年股市多空實戰經驗 法人圈基本面研究與自營操盤 型態戰法，掌握關鍵轉折 飆股重壓，讓你獲利極大化！','');
/*!40000 ALTER TABLE `consultants` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-06-07 13:13:31
