CREATE DATABASE `spotify` /*!40100 DEFAULT CHARACTER SET latin1 */;

-- spotify.audio definition

CREATE TABLE `audio` (
  `ts` datetime DEFAULT NULL,
  `username` text,
  `platform` tinytext,
  `ms_played` int(11) DEFAULT NULL,
  `conn_country` tinytext,
  `ip_addr_decrypted` text,
  `user_agent_decrypted` text,
  `master_metadata_track_name` text CHARACTER SET utf8,
  `master_metadata_album_artist_name` text CHARACTER SET utf8,
  `master_metadata_album_album_name` text CHARACTER SET utf8,
  `episode_name` text,
  `episode_show_name` text,
  `spotify_episode_uri` text,
  `reason_start` text,
  `reason_end` text,
  `shuffle` tinyint(1) DEFAULT NULL,
  `skipped` tinyint(1) DEFAULT NULL,
  `offline` tinyint(1) DEFAULT NULL,
  `offline_timestamp` text,
  `incognito_mode` text,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `spotify_track_uri` varchar(100) DEFAULT NULL,
  `year` int(11) DEFAULT NULL,
  `month` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=161872 DEFAULT CHARSET=latin1;