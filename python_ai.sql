SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 資料庫: `python_ai`
--
CREATE DATABASE `python_ai` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `python_ai`;

-- --------------------------------------------------------

--
-- 表的結構 `member`
--

CREATE TABLE IF NOT EXISTS `member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `birthday` date NOT NULL DEFAULT '0000-00-00',
  `address` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=23 ;

--
-- 轉存資料表中的資料 `member`
--

INSERT INTO `member` (`id`, `name`, `birthday`, `address`) VALUES
(1, '測試', '2018-11-01', '測試測試'),
(2, '測試2', '2018-11-22', '測試2測試2'),
(3, 'xxx', '2011-11-10', 'xxxxxx'),
(4, 'bbb', '2018-10-10', 'bbbbbb'),
(5, 'ccc', '2018-11-01', 'ccccc'),
(10, '實驗1', '2018-11-05', '實驗1'),
(11, '哈哈', '2011-11-11', '哈哈哈'),
(12, '測試你', '2010-10-21', '測試'),
(20, '您好', '2011-11-11', '您好歡迎光臨'),
(21, '測試測試', '1950-05-05', '測試測試AAAA'),
(22, '哈囉', '2010-10-10', '哈囉哈囉');

-- --------------------------------------------------------

--
-- 表的結構 `tel`
--

CREATE TABLE IF NOT EXISTS `tel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `member_id` int(11) NOT NULL,
  `tel` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `member_id` (`member_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=23 ;

--
-- 轉存資料表中的資料 `tel`
--

INSERT INTO `tel` (`id`, `member_id`, `tel`) VALUES
(1, 1, '1111-1111'),
(2, 1, '2222-2222'),
(9, 2, '9999-0000'),
(12, 2, '9999-0000'),
(13, 2, '9999-0000'),
(14, 2, '9999-0000'),
(22, 2, '9999-0000');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
