from bs4 import BeautifulSoup

markup = '''
<div class="tbody m-tcol-c" id="tbody" style="width:744px; padding-left:43px; padding-right:43px; margin-right:0px;">
					
					
					
					
					

					
					
					
					
						








    <script type="text/javascript" src="/static/js/mycafe/javascript/click/clickcr-1577769455000-6201.js"></script>


    
    

    
    
    
    

    
    
    
    
    
    

    







<script type="text/javascript" src="/static/js/mycafe/common/bastat/ScriptBAStatLog-1585128038000-108816.js" charset="UTF-8"></script>


<script type="text/javascript">
    var LOG_KEY = "CAFE_UUID";

    function uuidv4() {
		var uuid = "", i, random;
		for (i = 0; i < 32; i++) {
		random = Math.random() * 16 | 0;
		if (i == 8 || i == 12 || i == 16 || i == 20) {
		  uuid += "-"
		}
		uuid += (i == 12 ? 4 : (i == 16 ? (random & 3 | 8) : random)).toString(16);
		}
		return uuid;
    }

    function getDeviceId() {
    	try {
		  if (!localStorage.getItem(LOG_KEY)) {
			localStorage.setItem(LOG_KEY, uuidv4());
		  }

		  return localStorage.getItem(LOG_KEY);
		} catch (e) {
		  // silent
		  console.error("Can't access localStorage");
		  return "__UNKNOWN__";
		}
    }

    function getReferrerForBA() {
        if (typeof(window.top.articleReadBalog) === "undefined") {
            window.top.articleReadBalog = {
                useIframeReferrer: false
            };
        }
        if (!window.top.articleReadBalog.useIframeReferrer && !!window.top.document.referrer) {
            window.top.articleReadBalog.useIframeReferrer = true;
            return window.top.document.referrer;
        }
        return document.referrer;
    }

    var oBAStatSender = new cafe.BAStatSender({
        oClient : {
            service_id: 'cafe',
            user_key: 'markkorea',
            os_name: '__UNKNOWN__',
            os_ver: '-1',
            app_ver: '-1',
            country: 'XX',
            language: 'xx',
            device_id: getDeviceId(),
            device_model: '__UNKNOWN__',
            product: 'web'
        },
        sEnv: 'real'
    });
</script>

<script type="text/javascript">

function registrationComplete(paymentcorp) {
    return;
}

function showLoginPopup() {
    var redirectUrl = encodeURIComponent(encodeURIComponent(encodeURIComponent(location.pathname + location.search)));

    var oWnd = open_wnd('https://nid.naver.com/nidlogin.login?template=plogin&mode=form&url=http://cafe.naver.com/OpenerRedirect.nhn%3Fopenerurl%3D%252Fjoonggonara.cafe%253Femail%253D%2526iframe_url%253D' + redirectUrl, 'naver_login', 410, 280);

    if (!oWnd) {
        alert("선택하신 기능이 차단되었습니다.\n팝업 차단을 해지하신 후에 다시 시도해 주세요.");
    }
}

function joinCafe() {
    if (!!parent.joinCafe) {
        parent.joinCafe(location.pathname + location.search);
    }
}


function purchaseGroupProduct_745010597() {

    
    
    
        window.open("", "_blank");
    

}


function purchase_745010597() {

    
    
    
    
    
    
        
        var purchaseQuantity = 1;
        var purchaseUrl = "ItemPurchase.nhn?articleid=745010597&clubid=10050146&paymentCorp=&quantity=" + purchaseQuantity;
        open_window(purchaseUrl, 'Purchase', 400, 255, "toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=no,resizable=1") ;
    

    return;

}

function showPhoneNo_745010597(obj){
	var articleId = '745010597';
	var ajax = new Ajax('/MarketItemOtn.nhn',{
		method: 'POST',
		suspend : true,
		params : {'articleid' : articleId, 'clubid' : clubid},
	    onLoad: function(res) {
	    	var oRes;
			eval('oRes = ' + res.responseText);
			if(oRes.result == '0000'){
				var nTempOtn = oRes.otn.toString();
				$('oTnPhoneNo').innerHTML = nTempOtn.substr(0,4)+'-'+nTempOtn.substr(4,3)+'-'+nTempOtn.substr(7,4);//oRes.otn;
				$('oTnPeriod').innerHTML = oRes.checkout+" 까지";
				if (oRes.mobile == 'true') {
				    $('mobileIcon').style.display = "";
				} else {
					$('mobileIcon').style.display = "none";
				}

				var elLayer = $('oTnLayer');
				/*
				Element.setCSS(elLayer,{
					'top' : 50+'px',
					'left' : 20+'px'
				});
				*/
				Element.show(elLayer);
				var pos = Element.realPos(obj);
				elLayer.style.left =  (pos.left - elLayer.offsetWidth + 70) + 'px';
				elLayer.style.top = (pos.top + 20) + 'px';

			} else if (oRes.result == '1002') {
				alert("사용할 수 없는 번호입니다");
			} else {
				alert("일회용 안심번호를 불러오지 못했습니다.");
			}
		}
	});
	ajax.request();
};

/**
 * 최신글등록/판매완료 레이어 표
 * @param {Object} obj : 클릭한 node
 * @param {String} sLayerId : 표시할 레이어 id
 * @param {boolean} bLeftAlign : 클릭한 왼쪽 위치 기준 정렬
 * @param {boolean} bTopAlign : 클릭한 위쪽 위치 기준 정렬
 */
function showConfirmLayer_745010597(obj, sLayerId, bLeftAlign, bTopAlign){
	Element.hide('confirm_writenew_745010597');
	Element.hide('confirm_soldout_745010597');

	var elLayer = $( sLayerId );
	var pos = Element.realPos(obj);

	Element.show( sLayerId );

	var width = (elLayer.offsetWidth == 0) ? 167: elLayer.offsetWidth;
	var height = (elLayer.offsetHeight == 0) ? 300 : elLayer.offsetHeight;

	elLayer.style.left = pos.left + (bLeftAlign ? 0 : - width + obj.offsetWidth ) + 'px';
	elLayer.style.top = pos.top + (bTopAlign ? obj.offsetHeight + 10: - height - 10) + 'px';
}

/** 안전결제 사용안내 레이어 표시 */
function showSafetyPaymentGuideLayer(){
    var elLayer = $('safetyPaymentGuideLayer');
    if( elLayer.style.display == 'none' ) {
        elLayer.style.display = '';
    }else{
        elLayer.style.display = 'none';
    }
}

/** 레이어 보여주기 */
function showArticleLayer(elBtn, sLayerId) {
    var pos = Element.realPos(elBtn);
    var elLayer = $(sLayerId);
    if( elLayer.style.display == 'none' ) {
        elLayer.style.display = '';
        elLayer.style.top = (pos.top + 20) + 'px';
        elLayer.style.left = (pos.left - 190) + 'px';
    }else{
        elLayer.style.display = 'none';
    }
}

/**
 * 구매자 안전거래 팝업
 */
 function popupBuyEscrow(){
	 window.open("http://www.unicro.co.kr/escrow/reqBuyEscrow.jsp", "유니크로", "width=670,height=760,scrollbars");
}
/**
 * 사기정보조회
 */
 function showFraudLayer(elBtn, sLayerId , sCafeId ,  sPhoneNumber) {
	    var pos = Element.realPos(elBtn);
	    var elLayer = $(sLayerId);
	    if( elLayer.style.display == 'none' ) {
	        elLayer.style.display = '';
	        elLayer.style.top = (pos.top + 20) + 'px';
	        elLayer.style.left = (pos.left - 300) + 'px';
	    }else{
	        elLayer.style.display = 'none';
	    }
	    if(sPhoneNumber.length > 0) {
	    	FraudSearch(elBtn, sCafeId , sPhoneNumber);
	    }
}
 /**
  * 사기정보조회 ajax
  */
 function FraudSearch(event, cafeId){
	 FraudSearch(event, cafeId , '');
 }
/**
 * 사기정보조회 ajax
 */
 function FraudSearch(event, sCafeId , sPhoneNumber){
	 	var elFraudLayerBody = $('fraudLayerBody');
	 	var elInputbox = $('fraudLayerInputbox');
		var elFraudLayerList = $('fraudLayerList');
		var elFraudLayerAddinfo = $('fraudLayerAddinfo');
		var errorMessage = '<ul><li id="fraudLayerText" class="complain_commerce fraud_commerce"><span class="text_commerce">일시적인 오류가 발생했습니다. 잠시 후 다시 시도해주세요</span></span></li></ul>';


		var sKeyword = elInputbox.value;
		var nType = 1;
		if(typeof sPhoneNumber != 'undefined' && sPhoneNumber.length > 0) {
			sKeyword = sPhoneNumber;
			elInputbox.value = sPhoneNumber;
			nType = 2;
		}
		if(sKeyword.trim().length <= 0) {
			alert("전화번호 또는 계좌번호 입력해주세요.");
			return;
		}
		var regex = /^[0-9\-\s]+$/g;
		if(!regex.test(sKeyword)) {
			alert('숫자만 입력할 수 있습니다.');
			return;
		}
		var ajax = new Ajax('/FraudSearch.nhn?keyword='+sKeyword+'&clubid='+sCafeId+'&type='+nType+'&token=NU1aYVpyM2VLclBCUEo0L3BVd0dRUT09DQo',{
			method: 'GET',
			suspend : true,
		    onLoad: function(res) {
				var oJsonResult = JSON.parse(res.responseText);
				if (oJsonResult.message.status == 200) {
					var oResult = oJsonResult.message.result;
					if (typeof oResult.keyword == "undefined") {
						//elFraudLayerList.innerHTML = errorMessage;
						alert('숫자만 입력할 수 있습니다.');
						return;
					}
					if(oResult.count > 0) {
						elFraudLayerList.innerHTML = makeFraudInformationHTML('true',oResult.count);
					} else {
						elFraudLayerList.innerHTML =  makeFraudInformationHTML('false','0');
					}
					var sTimeKey = oResult.timeKey;
					elFraudLayerAddinfo.href = 'https://api.thecheat.co.kr/web/result.php?url=cafe.naver.com&keyword='+sKeyword+'&key='+sTimeKey;
					Element.removeClass(elFraudLayerBody,'ask_none');
					Element.show('fraudLayerAddinfo');
				} else {
					//elFraudLayerList.innerHTML = errorMessage;
					alert('숫자만 입력할 수 있습니다.');
					return;
				}

			}
		});
		ajax.request();
};

function makeFraudInformationHTML(isFraud , count) {
	var fraudInformationText = '<ul><li class="complain_commerce';
	if(isFraud == 'true') {
		fraudInformationText +=' fraud_commerce';
	}
	fraudInformationText +='">';
	fraudInformationText += '<span class="text_commerce">최근 3개월 내 사기 피해사례 <em>'+count+'</em>건</span>';
	fraudInformationText += '</li></ul>';
	fraudInformationText += '<p class="acgency_supply_commerce"><em>더치트</em> 제공 </p>';
	return 	fraudInformationText;
}

function npayRemit(obj) {
	var loggedIn = obj.getAttribute("data-loggedIn") == 'true';
	var cafemember = obj.getAttribute("data-cafemember") == 'true';
	var cafeId = obj.getAttribute("data-cafeId");
	var articleId = obj.getAttribute("data-articleId");
	var memberId = obj.getAttribute("data-memberId");
	var nickname = obj.getAttribute("data-nickname");
	var amount = obj.getAttribute("data-amount");

	if (!loggedIn) {
		showLoginPopup();
    } else if (!cafemember) {
        oBAStatSender.send([
            {
                eventType : cafe.BAStatEventType.PC_1777_450
            }
        ]);

        // 가입대기중
        if (false) {
            alert('이 기능은 카페 멤버만 사용할 수 있습니다.\n매니저의 가입 승인을 기다려주세요.');
            return;
        }

		if (confirm("이 기능은 카페 멤버만 사용할 수 있습니다. \n가입하시겠습니까?")) {
            oBAStatSender.send([
                {
                    eventType : cafe.BAStatEventType.PC_1778_450
                }
            ]);
			joinCafe();
		}
	} else {
		if (confirm('네이버페이 송금은 판매자에게 결제금액이\n바로 전달되는 직접거래입니다.\n판매자와 충분히 상의한 후 송금해주세요.\n' + nickname + '님에게 송금하시겠습니까?')) {
			var sUrl = "/npay/NpayRemitReserve.nhn?cafeId=" + cafeId
				+ "&memberId=" + memberId
				+ "&type=article"
				+ "&articleId=" + articleId
				+ "&amount=" + amount;

			window.open(sUrl, "npayremit", "width=465,height=820,scrollbars=yes");
		}
	}
}
</script>
    


	
	
		
			
			
				<div class="comm-foreign">
					<span>상품 구매시 주의해 주세요!</span>
					<p class="txt">중고나라에서 제안하는 안심거래 정보가 부족하여 위험도가 높은 게시글로 추정됩니다. <a target="_blank" href="http://cafe.naver.com/joonggonara/449728511">공지 확인하기 &gt;</a></p>
				</div>
			
		
	
	
	


    
    <table role="presentation" border="0" cellspacing="0" class="comm-detail ">
        <tbody><tr>
            
                <th class="image" scope="row">
                    <div class="image_condition">
                        <img src="https://cafefiles.pstatic.net/MjAyMDA0MjhfMTE3/MDAxNTg4MDA3MTMzMzEx.zJ8QDBy7tL9AmEV688oKAKeaCyOBUGsLLbzVyklDH7Yg.1h4UWG4Zn_r8QLkG8OUMPq05TE3htsUv8yoztlr7Iz0g.JPEG/13263405842462.jpg?type=s3" onclick="popview(this)" width="118" height="118" alt="" class="imgs border-sub" onerror="this.onerror='';this.src='https://ssl.pstatic.net/static/cafe/img_error_view.jpg'">
                        
                    </div>
                </th>
            
            <td class="details">
                <div class="details-m">
                        
                    
                        
                        <em class="sp_end sale_now" aria-label="판매" role="img"></em>
                        
                    

                    <p class="title">닌텐도 스위치 본체,게임 타이틀 전부팝니다 #3장무료배송</p>
                        
                    <div class="prod_price ">
                        <span class="cost">222,222<span class="won">원</span></span>
                    </div>
                    <table role="presentation" cellpadding="0" cellspacing="0" class="d-list">
                        <colgroup>
                            <col width="75">
                            <col>
                        </colgroup>
                        <tbody>
                            
                        
                            <tr title="판매자정보">
                                <th scope="row" class="border-sub">판매자정보</th>
                                <td class="border-sub seller_info">
                                    
                                        
                                        
                                            
                                        
                                    
                                    <span class="seller_email">
									
                                        
                                            <a href="mailto:dorlejd1@naver.com" class="m-tcol-c" id="bt_email">dorlejd1@naver.com</a>
                                        
                                        
                                    
								    </span>
                                    <span class="safety_deal_buy">
									<button class="safety_deal_btn" aria-label="안전거래 도움말" onclick="showArticleLayer(this, 'sellerInfoShowGuide'); return false;"><span class="sp_end safety_deal_help" role="img"></span></button>
								</span>
                                    <a href="#" class="sp_end fraud_check" title="사기정보조회" role="img" onclick="showFraudLayer(this, 'fraudLayer1' , '10050146' ,''); clickcr(this,'gdb.cheat','','',event); return false;"></a>
                                </td>
                            </tr>
                        
                        
                        
                            
                            <tr title="거래방법">
                                <th scope="row" class="border-sub">거래방법</th>
                                <td class="border-sub howtopay">
                                    <span class="add_row">직접거래</span>
                                    <a href="#" class="sp_end safe_deal" aria-label="안전거래신청" role="img" onclick="popupBuyEscrow(); clickcr(this,'gdb.safereq','','',event); return false;"></a>
                                    <span class="safety_deal_buy"><button class="safety_deal_btn" aria-label="안전거래 도움말" onclick="showArticleLayer(this, 'safetyPaymentGuideLayer'); return false;"><span class="sp_end safety_deal_help" role="img"></span></button></span>
                                </td>
                            </tr>
                        
                        <tr class="last-child" title="배송방법">
                            <th scope="row" class="border-sub">배송방법</th>
                            <td class="border-sub">판매자와 직접 연락하세요</td>
                        </tr>
                        </tbody>
                    </table>

                    
                        
                        
                        <div class="btns linenote border-sub">
                            


<span class="note">직접거래 시 아래 사항에 유의해주세요.</span>
<p class="m-tcol-c filter-60 tx_b_color">
    불확실한 판매자(본인 미인증, 해외IP, 사기의심 전화번호)의 물건은 구매하지 말아주세요.<br>
    판매자와의 연락은 메신저보다는 전화, 메일 등을 이용하시고 개인정보 유출에 주의하세요.<br>
    계좌이체 시 선입금을 유도할 경우 안전한 거래인지 다시 한 번 확인해주세요.
</p>

                        </div>
                        <div class="btns">
                            <p class="m-tcol-c filter-60">네이버에 등록된 판매 물품과 내용은 개별 판매자가 등록한 것으로서, <br>네이버카페는 등록을 위한 시스템만 제공하며 내용에 대하여 일체의 책임을 지지 않습니다.</p>
                        </div>
                    
                    
                    
                </div>
            </td>
        </tr>
    </tbody></table>

					
					
					
						



	<div class="banner_add">
		
		
		<a href="https://bit.ly/2Kz2F1m" target="_blank" onclick="clickcr(this, 'gdb.tban1', '', '', event);" banner="true"><img src="https://cafethumb.pstatic.net/MjAyMDA0MjdfMTM3/MDAxNTg3OTU0NzQ4MDgz.nAj4mDu947ik5sE6-KfQdJQ3pXrvtxigsL-SNIQNHYYg.H148103CLqKuSjz-hSmzTLaWNhAyGQ6Iz6Y1wUaet1Ig.PNG//sm%BD%BA%B8%C5%C6%BC%C4%CF%B9%E8%B3%CA_%282%29.png?type=f740_120_banner" alt="매니저 등록 배너"></a>
	</div>

						
 	<div class="notice_manager" id="noticeManagerArea">
 		<div id="noticeContentArea">* 거래전 필독! 주의하세요!
<br>* 연락처가 없이 외부링크, 카카오톡, 댓글로만 거래할 때
<br>* 연락처 및 계좌번호를 사이버캅과 더치트로 꼭 조회해보기
<br>* 업체인 척 위장하여 신분증과 사업자등록증을 보내는 경우
<br>* 고가의 물품(휴대폰,전자기기)등만 판매하고 최근(1주일 내) 게시글만 있을 때
<br>* 해외직구로 면세받은 물품을 판매하는 행위는 불법입니다.</div>
	</div>

					
					

					
					
					
						
						<br><img name="cafeuserimg" id="userImg157916856829799512" style="width:740px; height:740px;" onclick="popview(this)" src="https://cafeptthumb-phinf.pstatic.net/MjAyMDA0MjhfMTE3/MDAxNTg4MDA3MTMzMzEx.zJ8QDBy7tL9AmEV688oKAKeaCyOBUGsLLbzVyklDH7Yg.1h4UWG4Zn_r8QLkG8OUMPq05TE3htsUv8yoztlr7Iz0g.JPEG/13263405842462.jpg?type=w740"><br><span style="FONT-SIZE: 18pt"><span style="FONT-FAMILY: 돋움체, dotumche, applegothic"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 'Apple SD Gothic Neo', '맑은 고딕', 'Malgun Gothic', 돋움, dotum, sans-serif; WHITE-SPACE: normal; WORD-SPACING: 0px; TEXT-TRANSFORM: none; FLOAT: none; FONT-WEIGHT: 400; COLOR: rgb(34,34,34); FONT-STYLE: normal; ORPHANS: 2; WIDOWS: 2; DISPLAY: inline !important; LETTER-SPACING: normal; TEXT-INDENT: 0px; font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial"><span style="FONT-SIZE: 18pt"><span style="FONT-FAMILY: 돋움체, dotumche, applegothic"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 'Apple SD Gothic Neo', '맑은 고딕', 'Malgun Gothic', 돋움, dotum, sans-serif; WHITE-SPACE: normal; WORD-SPACING: 0px; TEXT-TRANSFORM: none; FLOAT: none; FONT-WEIGHT: 400; COLOR: rgb(34,34,34); FONT-STYLE: normal; ORPHANS: 2; WIDOWS: 2; DISPLAY: inline !important; LETTER-SPACING: normal; TEXT-INDENT: 0px; font-variant-ligatures: normal; font-variant-caps: normal; -webkit-text-stroke-width: 0px; text-decoration-style: initial; text-decoration-color: initial">&nbsp; 
<p style="TEXT-ALIGN: center" align="center"><strong><font size="5">닌텐도 스위치 중고 A급 판매 합니다.</font></strong></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><span style="FONT-SIZE: 36pt"></span></span></span>&nbsp;</font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><span style="FONT-SIZE: 36pt"><strong>번호:﻿010 257육 삼212</strong></span></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">안녕하세요.</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">닌텐도 스위치 다량 보유중 입니다.</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">상태는 철저한 검수와 테스트를 통해 모두 A급 입니다.</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">​</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">신형 구형 모두 준비 되어 있으며</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">타이틀또한 많이 준비되어 있습니다.</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">​</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">&nbsp;밑은 재고 현황입니다.</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 18pt; FONT-FAMILY: 돋움체, dotumche, applegothic">​직거래시 카드결제 가능합니다.</span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">​</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">&lt;스위치 본체 현황&gt;</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic">모든 제품은 중고 제품입니다 새제품이면미개봉이라고 씁니다.</span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">​</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">​닌텐도스위치 구형 네온/그레이 -&nbsp;34</font></strong></span></span></font></p>
<p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5">닌텐도스위치 18년 6월이전 제조품노박스 ㅡ 35&nbsp;</font></strong></span></span></font></p>
<p><font color="#222222"><span style="FONT-SIZE: 18pt"><span style="FONT-SIZE: 14pt; FONT-FAMILY: 돋움체, dotumche, applegothic"><strong><font color="#222222" size="5"></font></strong><strong><font color="#222222" size="5">
</font></strong></span></span></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><font color="#222222" size="5">닌텐도스위치 라이트&nbsp;- 품절</font></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>닌텐도스위치 신형 네온 ㅡ 44</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>닌텐도 스위치 신형 네온 노박스 ㅡ&nbsp;품절 </strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>카멜모니터 13인치 ㅡ 7.0<br>​</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>택배 구매시 택배비 0.5 추가됩니다&nbsp;안전거래시 수수료1만원별도입니다.</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&lt;타이틀 재고 현황&gt;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>원투스위치 ㅡ 3.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>원투스위치(표지만없음) ㅡ 3.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>루프란의 지하미궁 ㅡ 3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>다크소울 리마스터 ㅡ 3.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>레츠고피카츄 + 몬스터볼 셋트 ㅡ 4.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>배틀체이서 나이트워 ㅡ 2.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>피트니스복싱 ㅡ 3.5<br>젤다의 전설 야생의 숨결 ㅡ&nbsp;5.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>동물의 숲 ㅡ 7.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>&nbsp;<strong>젤다의전설 야생의숨결 가이드북 포함 ㅡ&nbsp;5.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>마블 얼티밋 얼라이언스 3 ㅡ3.5 </strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>드래곤 퀘스트 빌더즈 2 ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>루이지맨션3 ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>슈퍼 로봇대전T ㅡ 4.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>쿠니오군 더월드 ㅡ &nbsp;3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>슈퍼 마리오 오딧세이&nbsp;ㅡ&nbsp;4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>대난투&nbsp;ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>위쳐3 컴플리트 에디션 북미판 ㅡ 3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>위쳐3 컴플리트 에디션 정발판 ㅡ 5.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>포켓몬스터 소드 ㅡ 4.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>포켓몬스터 소드 미개봉 ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>포켓몬스터 실드 ㅡ 4.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>뉴슈퍼마리오U디럭스 ㅡ&nbsp;4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>드래곤퀘스트 11 ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>드래곤퀘스트11 미개봉 ㅡ&nbsp;5.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>젤다의전설 꿈꾸는 섬 ㅡ 4.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>요시크래프트 월드&nbsp;ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>요시크래프트 월드 미개봉 ㅡ&nbsp;5.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>포켓몬스터 레츠고 피카츄 ㅡ&nbsp;3.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>레츠고 피카츄 미개봉 ㅡ&nbsp;3.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px 0px 0px 80px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>레츠고 이브이 ㅡ 3.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>소드아트 온라인 할로우리얼라이제네이션 ㅡ&nbsp;3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>진격의거인2 ㅡ 3.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>스트리트 파이터 일판 ㅡ&nbsp;2.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>탐정진구지사부로&nbsp;프리즘오브아이즈&nbsp;+ 초회 CD&nbsp;ㅡ 3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>하츠네미쿠 프로젝트디바&nbsp;초회코드보유 ㅡ&nbsp;4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>스플래툰2 북미 ㅡ&nbsp;4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>스플래툰2 스타트에디션 ㅡ&nbsp;5.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>블러드스테인드 ㅡ 2.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>피파18 ㅡ 2.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>피파19 ㅡ 2.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>나의히어로원즈저스티스 ㅡ 3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>마리오카트 ㅡ 4.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>마리오카트+핸들두개 ㅡ 5.3</strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>문명6 미개봉 ㅡ 3.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>테일즈오브베스페리아리마스터 ㅡ 3.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>드래곤볼 제노버스2 북미 ㅡ 3.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>드래곤볼 파이터즈 ㅡ 3.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>디지몬스토리 사이버슬루스 ㅡ 4.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>슈퍼마리오메이커 2 ㅡ 4.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;디아블로3 ㅡ 5.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>마리오래비드킹덤(영판) ㅡ 2.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>슈퍼봄버맨 ㅡ 2.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>스낵월드 트레져러스 골드 ㅡ 3.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong><strong>포켓몬스터소드 알칩 3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>마리오 오딧세이 알칩 3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>무쌍오로치 알칩 2.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>레츠고피카츄 알칩 2.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>NBA 2k 20 알칩 2.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>스플래툰2 일판 알칩 3.5</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>&nbsp;</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>&nbsp;</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>﻿</strong><strong>(알칩은 칩케이스에 넣어서 보내드립니다)</strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong><strong>※ ﻿타이틀만 구매할시 택배비 0.3 추가 됩니다.</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;3장 이상 구매시 무료배송 해드립니다.</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&lt;주변기기 재고 현황&gt;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong>프로콘 노박스 ㅡ 5.0</strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>미니독 - 2.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>랜 네트워크 어댑터 - 2.0</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>마리오 오딧세이 파우치 -1.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;스플래툰 파우치 -1.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;유선 페이스오프 컨트롤러 마리오 에디션(정품)-3.5</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>직거래는 서울시 강북구 도봉로 45길 18ㅡ6 으로 오시면 됩니다.</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;&nbsp;&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;&nbsp;&nbsp; 오후 4시 이전에 구매건은 당일택배 접수 해드리며</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;&nbsp;&nbsp; 오후 4시 이후 택배건은 익일접수 해드립니다.</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>&nbsp;</strong></strong></font></p><p style="LIST-STYLE-TYPE: none; FONT-FAMILY: inherit; PADDING-BOTTOM: 0px; TEXT-ALIGN: center; PADDING-TOP: 0px; PADDING-LEFT: 0px; MARGIN: 0px; PADDING-RIGHT: 0px" align="center"><font color="#222222"><strong><strong>모든 문의는 안심번호나 01공-257육-삼212 로 부탁 드립니다.</strong></strong></font></p><p style="TEXT-ALIGN: center" align="center"><font color="#222222"><strong></strong></font></p></span></span><p></p></span></span>
<p></p></span></span>
					

					
					
					
					
				</div>
'''
content = BeautifulSoup(markup,"html.parser")

content.find(class_="comm-detail").decompose()
content.find(class_="banner_add").decompose()
content.find(class_="notice_manager").decompose()

print(content)