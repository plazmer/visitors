CREATE TABLE `visitors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groups` char(100) NOT NULL,
  `fio` char(100) NOT NULL,
  `datetime` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB CHARSET=utf8;
