from . import db

from sqlalchemy.dialects.mysql import BIGINT, VARCHAR, DATETIME


class Companies(db.Model):
    __tablename__ = "companies"
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }

    id = db.Column(BIGINT(11), primary_key=True)
    company_ko = db.Column(VARCHAR(255), nullable=True, comment="회사명 (한국어)")
    company_en = db.Column(VARCHAR(255), nullable=True, comment="회사명 (영어)")
    company_ja = db.Column(VARCHAR(255), nullable=True, comment="회사명 (일본어)")
    tag_ko = db.Column(VARCHAR(256), nullable=True, comment="회사 태그 (일본어)")
    tag_en = db.Column(VARCHAR(256), nullable=True, comment="회사 태그 (일본어)")
    tag_ja = db.Column(VARCHAR(256), nullable=True, comment="회사 태그 (일본어)")
    created_at = db.Column(DATETIME, nullable=False,
                           server_default=db.func.current_timestamp(),
                           comment='생성 시간')
    updated_at = db.Column(DATETIME, nullable=False,
                           server_default=db.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'),
                           comment='수정 시간')