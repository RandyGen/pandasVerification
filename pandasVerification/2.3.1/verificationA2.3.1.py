# 連続値のカウントを行うソースコード
import pandas as pd
import time
import random


def chk_dataframe_series(df):  # 比較するソースコード
    y = df['group']
    df['new'] = y.groupby((y != y.shift()).cumsum()).cumcount() + 1


if __name__ == '__main__':

    repeat_time = 10  # 繰り返す回数
    cum_execute_time = 0  # 累計処理時間
    dataframe_len = 100000  # Dataframeのindexの長さ　データサイズ

    for i in range(repeat_time):
        # データ作成
        random.seed(i)
        group_list = [random.randint(0, 10) for j in range(dataframe_len)]
        random.seed(i+1)
        value_list = [random.randint(0, 10) for j in range(dataframe_len)]
        sample_df = pd.DataFrame({'group': group_list,
                                  'value': value_list})

        start = time.time()  # 処理開始時間
        chk_dataframe_series(sample_df)
        end = time.time()  # 処理終了時間
        execute_time = end - start  # 1回の処理時間
        cum_execute_time += execute_time  # 累計処理時間
        print('one time runtime(', i+1, '):', execute_time)  # 1回の処理時間表示

    print('average runtime:', cum_execute_time/repeat_time)  # 10回の処理時間の平均表示
