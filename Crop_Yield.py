{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "eecf2850-7244-4ad0-8bfc-e3babe325d4a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import numpy as np\n",
    "from matplotlib import pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "04177f3b-4d81-4af0-8621-845573d42eb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv('crop_yield.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "9b8bed60-232e-43e0-8186-d3cb466e5f7e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Crop</th>\n",
       "      <th>Crop_Year</th>\n",
       "      <th>Season</th>\n",
       "      <th>State</th>\n",
       "      <th>Area</th>\n",
       "      <th>Production</th>\n",
       "      <th>Annual_Rainfall</th>\n",
       "      <th>Fertilizer</th>\n",
       "      <th>Pesticide</th>\n",
       "      <th>Yield</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Arecanut</td>\n",
       "      <td>1997</td>\n",
       "      <td>Whole Year</td>\n",
       "      <td>Assam</td>\n",
       "      <td>73814.0</td>\n",
       "      <td>56708</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>7024878.38</td>\n",
       "      <td>22882.34</td>\n",
       "      <td>0.796087</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Arhar/Tur</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>6637.0</td>\n",
       "      <td>4685</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>631643.29</td>\n",
       "      <td>2057.47</td>\n",
       "      <td>0.710435</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Castor seed</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>796.0</td>\n",
       "      <td>22</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>75755.32</td>\n",
       "      <td>246.76</td>\n",
       "      <td>0.238333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Coconut</td>\n",
       "      <td>1997</td>\n",
       "      <td>Whole Year</td>\n",
       "      <td>Assam</td>\n",
       "      <td>19656.0</td>\n",
       "      <td>126905000</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>1870661.52</td>\n",
       "      <td>6093.36</td>\n",
       "      <td>5238.051739</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Cotton(lint)</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>1739.0</td>\n",
       "      <td>794</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>165500.63</td>\n",
       "      <td>539.09</td>\n",
       "      <td>0.420909</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Dry chillies</td>\n",
       "      <td>1997</td>\n",
       "      <td>Whole Year</td>\n",
       "      <td>Assam</td>\n",
       "      <td>13587.0</td>\n",
       "      <td>9073</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>1293074.79</td>\n",
       "      <td>4211.97</td>\n",
       "      <td>0.643636</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Gram</td>\n",
       "      <td>1997</td>\n",
       "      <td>Rabi</td>\n",
       "      <td>Assam</td>\n",
       "      <td>2979.0</td>\n",
       "      <td>1507</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>283511.43</td>\n",
       "      <td>923.49</td>\n",
       "      <td>0.465455</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Jute</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>94520.0</td>\n",
       "      <td>904095</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>8995468.40</td>\n",
       "      <td>29301.20</td>\n",
       "      <td>9.919565</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Linseed</td>\n",
       "      <td>1997</td>\n",
       "      <td>Rabi</td>\n",
       "      <td>Assam</td>\n",
       "      <td>10098.0</td>\n",
       "      <td>5158</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>961026.66</td>\n",
       "      <td>3130.38</td>\n",
       "      <td>0.461364</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Maize</td>\n",
       "      <td>1997</td>\n",
       "      <td>Kharif</td>\n",
       "      <td>Assam</td>\n",
       "      <td>19216.0</td>\n",
       "      <td>14721</td>\n",
       "      <td>2051.4</td>\n",
       "      <td>1828786.72</td>\n",
       "      <td>5956.96</td>\n",
       "      <td>0.615652</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Crop  Crop_Year       Season  State     Area  Production  \\\n",
       "0      Arecanut       1997  Whole Year   Assam  73814.0       56708   \n",
       "1     Arhar/Tur       1997  Kharif       Assam   6637.0        4685   \n",
       "2   Castor seed       1997  Kharif       Assam    796.0          22   \n",
       "3      Coconut        1997  Whole Year   Assam  19656.0   126905000   \n",
       "4  Cotton(lint)       1997  Kharif       Assam   1739.0         794   \n",
       "5  Dry chillies       1997  Whole Year   Assam  13587.0        9073   \n",
       "6          Gram       1997  Rabi         Assam   2979.0        1507   \n",
       "7          Jute       1997  Kharif       Assam  94520.0      904095   \n",
       "8       Linseed       1997  Rabi         Assam  10098.0        5158   \n",
       "9         Maize       1997  Kharif       Assam  19216.0       14721   \n",
       "\n",
       "   Annual_Rainfall  Fertilizer  Pesticide        Yield  \n",
       "0           2051.4  7024878.38   22882.34     0.796087  \n",
       "1           2051.4   631643.29    2057.47     0.710435  \n",
       "2           2051.4    75755.32     246.76     0.238333  \n",
       "3           2051.4  1870661.52    6093.36  5238.051739  \n",
       "4           2051.4   165500.63     539.09     0.420909  \n",
       "5           2051.4  1293074.79    4211.97     0.643636  \n",
       "6           2051.4   283511.43     923.49     0.465455  \n",
       "7           2051.4  8995468.40   29301.20     9.919565  \n",
       "8           2051.4   961026.66    3130.38     0.461364  \n",
       "9           2051.4  1828786.72    5956.96     0.615652  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "3ac06a9d-c697-41e1-ae0e-406fca145aaa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Crop               0\n",
       "Crop_Year          0\n",
       "Season             0\n",
       "State              0\n",
       "Area               0\n",
       "Production         0\n",
       "Annual_Rainfall    0\n",
       "Fertilizer         0\n",
       "Pesticide          0\n",
       "Yield              0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isna().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "4f20bb7c-cc41-4331-8fe9-9fc05bf5c8db",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "19684    False\n",
       "19685    False\n",
       "19686    False\n",
       "19687    False\n",
       "19688    False\n",
       "Length: 19689, dtype: bool"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "34a690bf-c066-45ef-8dfd-9c1ce999d0be",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0        False\n",
       "1        False\n",
       "2        False\n",
       "3        False\n",
       "4        False\n",
       "         ...  \n",
       "19684     True\n",
       "19685     True\n",
       "19686     True\n",
       "19687     True\n",
       "19688     True\n",
       "Length: 19689, dtype: bool"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated('Crop')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "b61b7fda-9323-49dc-8e8a-b95520f9233d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.duplicated().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "fffe4dad-4fbe-4728-885c-48b70e88b405",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: ylabel='Crop'>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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GC1btqRz586UK1cOFxcXrl69muvav+apnjp1Cjc3N3R1dalQoQKZmZk8ePAAV1dXrdfLv263t7enb9++bN26la+++oply5YBULFiRS5duoSTk1Ou642NjSldujRqtZrY2Nhc53NGFj09PXPNIz516tRrvw87OztSU1OVz6arq8v69euV7YzHjBmDoaFhntf26NGD0NBQrekDL7OysuLZs2ckJycrx/5aCAO4u7szbNgw9u/fT5s2bZRFbTo6Oujq6molYyxbtozHjx8zffp06tatS61atYiPj3/tZ4TsCLFChQpp/Rk+efIkzz9nIYQQQhRMH3WRC9CuXTt0dXVZuHAhkD0P9Ndff+XEiRNERkbSp08f7t+/n+u62NhYhg8fTlRUFBs2bGD+/PkMGTIEyC7UfH196dq1K1u3buXmzZucOXOG4OBgdu3aBcDQoUPZt28fN2/e5LfffuPw4cN4enoC2YvSHj9+TMeOHTl79izR0dHs27eP7t27k5mZSeHChQkICGDYsGGsXr2a6OhofvvtN+bPn8/q1asB6Nu3L9euXWPEiBFERUWxfv16QkJCXvtdfPrpp9SoUYMOHTooi7n27t3L3bt3MTY2Zv369Tx//jzPa3v16sXDhw/p2bNnnuerVauGkZERo0ePJjo6Old/UlJSGDhwIKGhody6dYuwsDDOnj2rfCcmJiZkZmZy6dIlDA0N+eyzz6hbty4qlYr58+dz9OhRVCoVY8aMUe556dIlAgMDgex/UNSqVYvo6GhMTEzw9/enb9++ODo6olarcXBw0MrSFUIIIUTB9tEXuXp6egwcOJBvvvmG5ORkxo4dS8WKFfHx8aFu3bpYW1vTqlWrXNd17dqVlJQUqlatyoABAxgyZAi9e/dWzq9atYquXbvy1Vdf4eHhQatWrTh79iwODg5A9tzfAQMG4OnpSePGjXF3d2fRokUA2NraEhYWRmZmJp999hleXl4MHToUc3NzdHSyv/LJkyczbtw4goODlXvs2rVLybR1cHBgy5YtbN++nXLlyrF48WKthWx5UalU7N27ly+++ILhw4dTunRpAgMD8ff35+rVq9y7dw9fX1+ysrLy/B6LFi2qbPDwV0WKFGHt2rXs3r1biWWbOHGicl5XV5f4+Hi6du2Ku7s77du3p0mTJspCr2LFiuHk5ESHDh2wsrIiICCA8+fPU7Jk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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(df['Crop'])\n",
    "# sns.boxplot(df['Crop_Year'])\n",
    "# sns.boxplot(df['Season'])\n",
    "# sns.boxplot(df['State'])\n",
    "# sns.boxplot(df['Area'])\n",
    "# sns.boxplot(df['Production'])\n",
    "# sns.boxplot(df['Annual_Rainfall'])\n",
    "# sns.boxplot(df['Fertilizer'])\n",
    "# sns.boxplot(df['Pesticide'])\n",
    "# sns.boxplot(df['Yield'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0ab43c4d-f7ab-422a-9abb-b77b287b953a",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\vinit\\AppData\\Local\\Temp\\ipykernel_21860\\1930570014.py:2: UserWarning: \n",
      "\n",
      "`distplot` is a deprecated function and will be removed in seaborn v0.14.0.\n",
      "\n",
      "Please adapt your code to use either `displot` (a figure-level function with\n",
      "similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "\n",
      "For a guide to updating your code to use the new functions, please see\n",
      "https://gist.github.com/mwaskom/de44147ed2974457ad6372750bbe5751\n",
      "\n",
      "  sns.distplot(df['Season'])\n"
     ]
    },
    {
     "ename": "ValueError",
     "evalue": "could not convert string to float: 'Whole Year '",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[9], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m plt\u001b[38;5;241m.\u001b[39msubplot(\u001b[38;5;241m1\u001b[39m,\u001b[38;5;241m2\u001b[39m,\u001b[38;5;241m1\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m \u001b[43msns\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mdistplot\u001b[49m\u001b[43m(\u001b[49m\u001b[43mdf\u001b[49m\u001b[43m[\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mSeason\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m]\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\seaborn\\distributions.py:2443\u001b[0m, in \u001b[0;36mdistplot\u001b[1;34m(a, bins, hist, kde, rug, fit, hist_kws, kde_kws, rug_kws, fit_kws, color, vertical, norm_hist, axlabel, label, ax, x)\u001b[0m\n\u001b[0;32m   2440\u001b[0m     a \u001b[38;5;241m=\u001b[39m x\n\u001b[0;32m   2442\u001b[0m \u001b[38;5;66;03m# Make a a 1-d float array\u001b[39;00m\n\u001b[1;32m-> 2443\u001b[0m a \u001b[38;5;241m=\u001b[39m \u001b[43mnp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43masarray\u001b[49m\u001b[43m(\u001b[49m\u001b[43ma\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mfloat\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m   2444\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m a\u001b[38;5;241m.\u001b[39mndim \u001b[38;5;241m>\u001b[39m \u001b[38;5;241m1\u001b[39m:\n\u001b[0;32m   2445\u001b[0m     a \u001b[38;5;241m=\u001b[39m a\u001b[38;5;241m.\u001b[39msqueeze()\n",
      "File \u001b[1;32m~\\AppData\\Local\\Programs\\Python\\Python311\\Lib\\site-packages\\pandas\\core\\series.py:917\u001b[0m, in \u001b[0;36mSeries.__array__\u001b[1;34m(self, dtype)\u001b[0m\n\u001b[0;32m    870\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    871\u001b[0m \u001b[38;5;124;03mReturn the values as a NumPy array.\u001b[39;00m\n\u001b[0;32m    872\u001b[0m \n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    914\u001b[0m \u001b[38;5;124;03m      dtype='datetime64[ns]')\u001b[39;00m\n\u001b[0;32m    915\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[0;32m    916\u001b[0m values \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_values\n\u001b[1;32m--> 917\u001b[0m arr \u001b[38;5;241m=\u001b[39m np\u001b[38;5;241m.\u001b[39masarray(values, dtype\u001b[38;5;241m=\u001b[39mdtype)\n\u001b[0;32m    918\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m using_copy_on_write() \u001b[38;5;129;01mand\u001b[39;00m astype_is_view(values\u001b[38;5;241m.\u001b[39mdtype, arr\u001b[38;5;241m.\u001b[39mdtype):\n\u001b[0;32m    919\u001b[0m     arr \u001b[38;5;241m=\u001b[39m arr\u001b[38;5;241m.\u001b[39mview()\n",
      "\u001b[1;31mValueError\u001b[0m: could not convert string to float: 'Whole Year '"
     ]
    },
    {
     "data": {
      "image/png": "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84fnANXX1yscDquqqkp79+7V/PnzVVxcrCNHjgx6fnNzs2699Va98847amlpUTAY1A033KAvvvjiew8PYGJLcc45LxsKCwt17bXXatu2bZKkRCKhYDCo++67T2vWrPnO/X19fZo+fbq2bdumsrKyQc/p6elRT09P8ud4PK5gMKhYLKaMjAwv4wIYAfF4XJmZmSN+H/T0CKi3t1etra0KhUJf30BqqkKhkFpaWs7qNk6cOKFTp07poosuGvKc6upqZWZmJo9gMOhlTAAThKcAdXV1qa+vT4FAoN96IBBQJBI5q9tYvXq1ZsyY0S9i31RZWalYLJY8Ojs7vYwJYIKYNJYX27x5s3bt2qXm5malp6cPeZ7f75ff7x/DyQBY8BSgrKwspaWlKRqN9luPRqPKycn51r1btmzR5s2b9fbbb2vevHneJwVwzvH0FMzn86mgoEBNTU3JtUQioaamJhUVFQ2574knntDGjRvV2NioBQsWDH9aAOcUz0/BwuGwysvLtWDBAi1cuFA1NTXq7u7WypUrJUllZWWaOXOmqqurJUm///3vtX79er344ovKy8tLvlZ04YUX6sILLxzBXwXAROM5QKWlpTp69KjWr1+vSCSi/Px8NTY2Jl+Y7ujoUGrq1w+snnrqKfX29uoXv/hFv9upqqrSI4888v2mBzChef4ckIXR+gwCgLMzLj4HBAAjiQABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAGQIEwAwBAmCGAAEwQ4AAmCFAAMwQIABmCBAAMwQIgBkCBMAMAQJghgABMEOAAJghQADMECAAZggQADMECIAZAgTADAECYIYAATBDgACYIUAAzBAgAGYIEAAzBAiAmWEFqLa2Vnl5eUpPT1dhYaH27Nnzref/9a9/1WWXXab09HRdffXVamhoGNawAM4tngNUX1+vcDisqqoq7d27V/Pnz1dxcbGOHDky6PkffPCBbr31Vt1+++3at2+fli1bpmXLlumjjz763sMDmNhSnHPOy4bCwkJde+212rZtmyQpkUgo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",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.subplot(1,2,1)\n",
    "sns.distplot(df['Season'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6e1c486-8c42-4d14-9b08-4df0a4b2532b",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(df['State'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ee770b05-c216-4eed-9890-beec6db86b3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(df['Area'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48242ec2-71c8-414b-9ebb-a2bdd804ee09",
   "metadata": {},
   "outputs": [],
   "source": [
    "Q1=df['Area'].quantile(0.25)\n",
    "Q3=df['Area'].quantile(0.45)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e89b6eb-4c5f-44c8-a6c4-41dffbb4335d",
   "metadata": {},
   "outputs": [],
   "source": [
    "IQR=Q3-Q1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b78131d-047f-4dea-a70d-3b1ce589a46c",
   "metadata": {},
   "outputs": [],
   "source": [
    "min=Q1-1.5*IQR\n",
    "max=Q3+1.5*IQR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b725a438-a79c-40bf-a98b-9e739a0a47a4",
   "metadata": {},
   "outputs": [],
   "source": [
    "min"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5bf80ed9-92ae-4e38-952c-e33dd0ce4a44",
   "metadata": {},
   "outputs": [],
   "source": [
    "max"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d7f57ef-abf7-4878-83cb-e9e7bc85387d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=df[(df['Area']>min)&(df['Area']<max)]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4e152823-0cf3-4a16-850c-3d6d0b162e0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.boxplot(df['Area'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96767146-7ff9-4165-8495-f1a603dd1e26",
   "metadata": {},
   "outputs": [],
   "source": [
    "numeric_df = df.select_dtypes(include=['number'])\n",
    "\n",
    "# Calculate quartiles and IQR for each numeric column\n",
    "Q1 = numeric_df.quantile(0.25)\n",
    "Q3 = numeric_df.quantile(0.75)\n",
    "IQR = Q3 - Q1\n",
    "\n",
    "# Calculate min and max values for outlier removal\n",
    "min_values = Q1 - 1.5 * IQR\n",
    "max_values = Q3 + 1.5 * IQR\n",
    "\n",
    "# Apply outlier removal for each numeric column directly to df\n",
    "for column in ['Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Yield']:\n",
    "    df = df[(df[column] > min_values[column]) & (df[column] < max_values[column])]\n",
    "\n",
    "# Plot boxplots for each numeric column in the cleaned DataFrame\n",
    "plt.figure(figsize=(12, 8))\n",
    "for i, column in enumerate(['Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide', 'Yield'], start=1):\n",
    "    plt.subplot(2, 3, i)\n",
    "    sns.boxplot(df[column])\n",
    "    plt.title(f'Boxplot of {column}')\n",
    "    plt.ylabel('Values')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "c231236f-743c-42f2-a17d-e646b9e92422",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Shape of X_train: (15751, 97)\n",
      "Shape of X_test: (3938, 97)\n",
      "Shape of y_train: (15751,)\n",
      "Shape of y_test: (3938,)\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# Assuming df is your DataFrame containing the dataset\n",
    "\n",
    "# Perform one-hot encoding on categorical columns\n",
    "df_encoded = pd.get_dummies(df, columns=['Crop', 'State', 'Season'])\n",
    "\n",
    "# Define features (X) and target variable (y)\n",
    "X = df_encoded.drop(columns=['Yield'])  # Features are all columns except 'Yield'\n",
    "y = df_encoded['Yield']  # Target variable is 'Yield'\n",
    "\n",
    "# Split the dataset into training and testing sets (80% train, 20% test)\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "# Check the shape of the training and testing sets\n",
    "print(\"Shape of X_train:\", X_train.shape)\n",
    "print(\"Shape of X_test:\", X_test.shape)\n",
    "print(\"Shape of y_train:\", y_train.shape)\n",
    "print(\"Shape of y_test:\", y_test.shape)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "29820597-bd3c-4056-80a6-3627a77d959c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mean Squared Error: 9831.606748464777\n",
      "R-squared Score: 0.9877295087537968\n",
      "Accuracy: 0.9877295087537968\n"
     ]
    }
   ],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "\n",
    "# Initialize the Random Forest regressor\n",
    "rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)\n",
    "\n",
    "# Train the model on the training data\n",
    "rf_regressor.fit(X_train, y_train)\n",
    "\n",
    "# Predict crop yield on the testing data\n",
    "y_pred = rf_regressor.predict(X_test)\n",
    "\n",
    "# Calculate mean squared error\n",
    "mse = mean_squared_error(y_test, y_pred)\n",
    "print(\"Mean Squared Error:\", mse)\n",
    "\n",
    "# Calculate R-squared score\n",
    "r2 = r2_score(y_test, y_pred)\n",
    "print(\"R-squared Score:\", r2)\n",
    "\n",
    "# Calculate accuracy\n",
    "accuracy = rf_regressor.score(X_test, y_test)\n",
    "print(\"Accuracy:\", accuracy)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a9b7931-e205-4e4e-a2f5-2d94d042a2d9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
