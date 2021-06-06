-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2021-05-06 05:20:52
-- 伺服器版本： 10.4.18-MariaDB
-- PHP 版本： 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `2021_05_06`
--
CREATE DATABASE IF NOT EXISTS `2021_05_06` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `2021_05_06`;

-- --------------------------------------------------------

--
-- 資料表結構 `news`
--

CREATE TABLE `news` (
  `id` int(11) NOT NULL,
  `title` varchar(30) NOT NULL,
  `source` varchar(10) NOT NULL,
  `description` text NOT NULL,
  `create_time` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `news`
--

INSERT INTO `news` (`id`, `title`, `source`, `description`, `create_time`) VALUES
(1, '農訓協會攜手緯育TibaMe 打造農漁業線上學習庫', '經濟日報', '新冠疫情後，更加速各產業導入數位的決心。農訓協會與緯育TibaMe for Business合作導入線上學習資源與數位課程製作服務，服務全台及離島超過340家農漁會，今年開始部份實體培訓轉為線上，打造全台最大「農漁業零距離學習庫」，在疫情影響下學習不停擺!', '2021-04-13'),
(2, '職場》轉職5G、AI好難？非本科入門磚就看這塊', '中時新聞網', '隨著科技發展，5G、AI產業正夯，一併帶動周邊產業發展，就有資工系畢業的網友原本想搭上這一波風潮，謀求新職，沒想到卻因為大學4年對於程式語言並不專精，在前往相關企業面試時，遭到面試官洗臉。', '2021-04-14'),
(3, '緯育TibaMe攜六企業辦Beyond數位力年會', '經濟日報', '人才在數位時代、如何保有創新創造機會？緯創集團旗下緯育TibaMe昨(14)日舉辦Beyond數位力年會，Google台灣區前董事總經理簡立峰強調，疫情驅動零接觸經濟，當全球在數位連接世界與工作時，我們準備好了嗎？', '2021-01-15');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `news`
--
ALTER TABLE `news`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `news`
--
ALTER TABLE `news`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
