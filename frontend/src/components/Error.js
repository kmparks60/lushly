import React from 'react'
import {Link} from 'react-router-dom'
import Button from '@mui/material/Button'

function Error() {
  return (
    <>
        Error 404<br/>
        Page Not Found<br/>
        <Button component={Link} variant='Contained' to='/'>
            Home
        </Button>
    </>
  )
}

export default Error
