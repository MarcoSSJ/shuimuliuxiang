<template>
    <view class="page">
        <view class="search1">
            <input class="textBar" v-model="searchText">
            <view class="searchButton" @click="search()">搜索</view>
        </view>
        <view class="search2">
            <view v-for="searchFlag in searchFlags" :key="searchFlag.id" :class="searchFlag.picked ? 'searchFlag1' : 'searchFlag2'" @click="searchFlagChange(searchFlag)">{{searchFlag.value}}</view>
        </view>
        <view class="activity1">
            <view v-for="activityType in activityTypes" :key="activityType.id" :class="activityType.picked ? 'activityType1' : 'activityType2'" @click="activityTypeChange(activityType)">{{activityType.value}}</view>
        </view>
        <view class="activity2">
            <view v-for="sortFlag in sortFlags" :key="sortFlag.id" :class="sortFlag.picked ? 'sortFlag1' : 'sortFlag2'" @click="sortFlagChange(sortFlag)">{{sortFlag.value}}</view>
        </view>
        <view class="activity3">
            <view class="activity3" v-if="pageAll > 0">
                <view class="activity3" v-for="activity in activities" :key="activity.id" @click="toActivityDetails(activity.number)">
                    <activitybox :activity="activity"></activitybox>
                </view>
            </view>
        </view>
        <view class="activity4">
            <view @click="lastPage()">上一页</view>
            <view v-if="pageAll > 0">{{pageNum}} / {{pageAll}}</view>
            <view v-else>1 / 1</view>
            <view @click="nextPage()">下一页</view>
        </view>
    </view>
</template>

<script>
import qcloud from 'wafer2-client-sdk'
import config from '@/config.js'
import activitybox from "@/components/activityBox"
export default {
    components:{
        activitybox
    },

    created() {
        console.log('activitypage ready');
    },

    onShow() {
        var _this = this;
        wx.request({
            url:config.activityInfo,
            dataType: "json",
            data: {
                openID:_this.GLOBAL.openid,
                searchKeyword:_this.searchKeyWord,
                searchFlag:_this.searchFlag,
                activityType:_this.activityType,
                sortFlag:_this.sortFlag,
                pageNum:_this.pageNum,
            },
            method: 'POST',
            header: { 'content-type': 'application/x-www-form-urlencoded'},
            success: function (res) {
                if (res.statusCode == 200) {
                    if(res.data.error){

                    }
                    else{
                        _this.activities = res.data.content;
                        _this.pageAll = res.data.page;
                    }
                }
                else {
                    console.log(res.errMsg);
                }
                console.log(res)
            },
        })
    },

    data() {
        return {
            searchText:"",
            searchKeyWord:"",
            searchFlag:"name",
            searchFlags:[
                { name: 'name', value: '活动名称', picked: true},
                { name: 'owner', value: '活动发起方', picked: false},
            ],
            activityType:[
                '0','1','2','3','4','5'
            ],
            activityTypes:[
                { code: '0', value: '文化教育', picked: true},
                { code: '1', value: '赛会服务', picked: true},
                { code: '2', value: '社区服务', picked: true},
                { code: '3', value: '医疗卫生', picked: true},
                { code: '4', value: '健康残障', picked: true},
                { code: '5', value: '其他类型', picked: true},
            ],
            sortFlag: "time",
            sortFlags:[
                { name: 'time', value: '时间', picked: true},
                { name: 'hot', value: '热度', picked: false},
                { name: 'notFull', value: '未招满', picked: false},
            ],
            activities:[

            ],
            pageNum: 1,
            pageAll: 1,
        }
    },

    methods: {
        search(){
            var _this = this;
            _this.searchKeyWord = _this.searchText;
            for(var i in _this.searchFlags)
            {
                if(_this.searchFlags[i].picked == true)
                {
                    _this.searchFlag = _this.searchFlags[i].name;
                }
            }
            _this.pageNum = 1;
            _this.$mp.page.onShow();
        },
        searchFlagChange(searchFlag){
            var _this = this;
            for(var i in _this.searchFlags)
            {
                _this.searchFlags[i].picked = false;
            }
            searchFlag.picked = true;
        },
        activityTypeChange(activityType){
            var _this = this;
            var activityTypes = [];
            activityType.picked = !activityType.picked;
            for(var i in _this.activityTypes)
            {
                if(_this.activityTypes[i].picked == true)
                {
                    activityTypes.push(_this.activityTypes[i].code);
                }
            }
            _this.activityType = activityTypes;
            _this.pageNum = 1;
            _this.$mp.page.onShow();
        },
        sortFlagChange(sortFlag){
            var _this = this;
            for(var i in _this.sortFlags)
            {
                _this.sortFlags[i].picked = false;
            }
            sortFlag.picked = true;
            _this.sortFlag = sortFlag.name;
            _this.pageNum = 1;
            _this.$mp.page.onShow();
        },
        lastPage(){
            var _this = this;
            if(_this.pageAll > 0 && _this.pageNum > 1)
            {
                _this.pageNum -= 1;
                _this.$mp.page.onShow();
            }
        },
        nextPage(){
            var _this = this;
            if(_this.pageAll > 0 && _this.pageNum < _this.pageAll)
            {
                _this.pageNum += 1;
                _this.$mp.page.onShow();
            }
        },
        toActivityDetails(activityNum){
            wx.navigateTo({url: '../activityDetails/main?activityNum='+activityNum});
        },
    },
}
</script>

<style>
.page {
    width: 750rpx;
    height: 1050rpx;
    margin: auto;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
}

.search1 {
    width: 600rpx;
	height: 80rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.search2 {
    width: 600rpx;
	height: 70rpx;
    font-size: 30rpx;
    color: #000;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activity1 {
    width: 600rpx;
    height: 120rpx;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items: center;
    align-content: space-around;
}

.activity2 {
    width: 600rpx;
    height: 70rpx;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.activity3 {
    width: 600rpx;
    height: 640rpx;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
}

.activity4 {
    width: 700rpx;
    height: 60rpx;
    font-size: 35rpx;
    color: rgb(122, 114, 189);
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items: center;
}

.textBar {
    width: 450rpx;
    height: 66rpx;
    font-size: 40rpx;
    color: #000;
    border: 2rpx solid rgb(122, 114, 189);
}

.searchButton {
    width: 150rpx;
    height: 70rpx;
    font-size: 40rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border-radius: 0;
    display: flex;
    justify-content: center;
    align-items: center;
}

.searchFlag1 {
    width: 270rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.searchFlag2 {
    width: 270rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.activityType1 {
    width: 180rpx;
    height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(122, 114, 189);
    border: 2rpx solid rgb(122, 114, 189);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.activityType2 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(122, 114, 189);
    border: 2rpx solid rgb(122, 114, 189);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.sortFlag1 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: #fff;
    background-color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}

.sortFlag2 {
    width: 180rpx;
	height: 50rpx;
    font-size: 30rpx;
    color: rgb(21, 174, 103);
    border: 2rpx solid rgb(21, 174, 103);
    border-radius: 15rpx;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
}
</style>