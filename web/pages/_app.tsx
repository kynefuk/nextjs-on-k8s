import '../styles/globals.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import type { AppProps } from 'next/app';
import axios from 'axios';
import {SWRConfig} from 'swr'

const MyApp: React.FC<AppProps> = ({ Component, pageProps }) => {
  return (
    <SWRConfig value={
      {
        fetcher: (url: string) => axios(url).then(res => res.data),
        dedupingInterval: 5000, // interval
        onSuccess: () => console.log('onSuccess')
      }
    }>
      <Component {...pageProps} />
    </SWRConfig>
  )
}

export default MyApp
